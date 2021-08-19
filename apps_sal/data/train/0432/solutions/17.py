class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = collections.Counter(nums)
        q = collections.deque()
        while c:
            for key in c:
                if key - 1 not in c:
                    q.append(key)
            while q:
                cur = q.popleft()
                pushed = False
                for nxt in range(cur + 1, cur + k):
                    if c[nxt] < c[cur]:
                        return False
                    c[nxt] -= c[cur]
                    if c[nxt] == 0:
                        c.pop(nxt)
                    if not pushed and c[nxt] != 0:
                        pushed = True
                        q.append(nxt)
                c.pop(cur)
        return True if not c else False

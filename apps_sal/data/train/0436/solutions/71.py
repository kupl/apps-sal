class Solution:

    def minDays(self, n: int) -> int:
        q = collections.deque()
        q.append(n)
        lvl = 0
        seen = set()
        while q:
            size = len(q)
            for _ in range(size):
                num = q.popleft()
                if num == 0:
                    return lvl
                seen.add(num)
                if num % 3 == 0 and num // 3 not in seen:
                    q.append(num // 3)
                if num % 2 == 0 and num // 2 not in seen:
                    q.append(num // 2)
                if num - 1 not in seen:
                    q.append(num - 1)
            lvl += 1

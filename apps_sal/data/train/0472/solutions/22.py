class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        seen = set()

        def steps(i):
            for next in [i + arr[i], i - arr[i]]:
                if next >= 0 and next < len(arr) and next not in seen:
                    seen.add(next)
                    yield next

        q = collections.deque()

        q.append(start)

        while q:
            c = q.popleft()
            for next in steps(c):
                if arr[next] == 0:
                    return True
                q.append(next)
        return False

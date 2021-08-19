class Solution:

    def minDays(self, n: int) -> int:
        q = deque()
        q.append((n, 0))
        visited = set()
        visited.add(n)
        while q:
            (cur, numSteps) = q.popleft()
            if cur == 0:
                return numSteps
            if cur - 1 not in visited:
                q.append((cur - 1, numSteps + 1))
                visited.add(cur - 1)
            if cur % 2 == 0 and cur // 2 not in visited:
                q.append((cur // 2, numSteps + 1))
                visited.add(cur // 2)
            if cur % 3 == 0 and cur // 3 not in visited:
                q.append((cur // 3, numSteps + 1))
                visited.add(cur // 3)
        return 0

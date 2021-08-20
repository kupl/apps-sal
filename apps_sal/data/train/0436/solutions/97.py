class Solution:

    def minDays(self, n: int) -> int:
        days = 0
        fringe = deque([n])
        seen = set()
        while fringe:
            for _ in range(len(fringe)):
                n = fringe.popleft()
                if n == 0:
                    return days
                if n - 1 not in seen:
                    fringe.append(n - 1)
                    seen.add(n - 1)
                if n % 2 == 0 and n // 2 not in seen:
                    fringe.append(n // 2)
                    seen.add(n // 2)
                if n % 3 == 0 and n // 3 not in seen:
                    fringe.append(n // 3)
                    seen.add(n // 3)
            days += 1

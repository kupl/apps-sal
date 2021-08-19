class Solution:

    def minDays(self, n: int) -> int:
        if n <= 0:
            return 0
        q = [n]
        ans = 0
        visited = {n}
        while q:
            size = len(q)
            for _ in range(size):
                i = q.pop(0)
                if i == 1:
                    return ans + 1
                if i % 3 == 0:
                    next = i - 2 * i // 3
                    if next not in visited:
                        q.append(next)
                        visited.add(next)
                if i % 2 == 0:
                    next = i // 2
                    if next not in visited:
                        q.append(next)
                        visited.add(next)
                if i - 1 not in visited:
                    q.append(i - 1)
                    visited.add(i - 1)
            ans += 1
        return 0

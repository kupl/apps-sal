from collections import deque


class Solution:
    def minDays(self, n: int) -> int:
        q1 = deque([0, None])
        q2 = deque([n, None])
        visited1 = {0}
        visited2 = {n}

        for i in range(n):
            while True:
                n = q1.popleft()
                if n is None:
                    q1.append(None)
                    break
                for m in [n + 1, n * 2, n * 3]:
                    if m in visited2:
                        return i * 2 + 1
                    if m not in visited1:
                        visited1.add(m)
                        q1.append(m)

            while True:
                n = q2.popleft()
                if n is None:
                    q2.append(None)
                    break
                l = [n - 1]
                if n % 2 == 0:
                    l.append(n // 2)
                if n % 3 == 0:
                    l.append(n // 3)
                for m in l:
                    if m in visited1:
                        return i * 2 + 2
                    if m not in visited2:
                        visited2.add(m)
                        q2.append(m)

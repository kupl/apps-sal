class Solution:
    def minDays(self, n: int) -> int:
        q = collections.deque([n])
        day = 0
        visited = set([n])
        while q:
            day += 1
            l = len(q)
            for i in range(l):
                tmp = q.popleft()
                if tmp - 1 not in visited:
                    if tmp - 1 == 0:
                        return day
                    visited.add(tmp - 1)
                    q.append(tmp - 1)
                if tmp % 2 == 0 and tmp / 2 not in visited:
                    visited.add(tmp / 2)
                    q.append(tmp / 2)
                if tmp % 3 == 0 and tmp / 3 not in visited:
                    visited.add(tmp / 3)
                    q.append(tmp / 3)

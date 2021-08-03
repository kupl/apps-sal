class Solution:
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n

        q = collections.deque()
        q.append([n, 0])
        visited = set([n])
        while len(q) > 0:
            x, d = q.popleft()
            if x == 0:
                return d

            neighbors = [x - 1]
            if x % 2 == 0:
                neighbors.append(x // 2)
            if x % 3 == 0:
                neighbors.append(x // 3)

            for y in neighbors:
                if y in visited:
                    continue
                q.append([y, d + 1])
                visited.add(y)

        g = {1: 1}
        x = 1
        for i in range(0, 30):
            for j in range(0, 20):
                x = (2**i) * (3**j)
                if x <= 1000000000:
                    g[x] = i + j
        days = 0
        while n > 1 and n not in g:
            days += 1
            n -= 1
        if n in g:
            days += g[n]
        return days

        f = [None] * (n + 1)
        f[1] = 1
        for k in range(2, n + 1):
            f[k] = 1 + f[k - 1]
            if k % 2 == 0:
                f[k] = min(f[k], 1 + f[k // 2])
            if k % 3 == 0:
                f[k] = min(f[k], 1 + f[k // 3])
        return f[n]

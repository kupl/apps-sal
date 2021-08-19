class Solution:

    def findSum(self, n, m, k):
        res = []
        s = m * n
        hi = min(n, m)
        border = max(n, m)
        path = [1] * k
        while path[0] <= hi:
            i = k - 1
            while i >= 0 and path[i] >= hi:
                i -= 1
            if i == -1 or path[i] >= hi:
                return res
            path[i] += 1
            path[i + 1:] = [path[i]] * (k - i - 1)
            if path[k - 1] + path[k - 2] > border:
                path[i:] = [hi] * (k - i)
                continue
            if sum((x * x for x in path)) == s:
                x = path[:]
                x.reverse()
                res.append(x)
        return res

    def hasNoOverLap(self, x1, y1, s1, x2, y2, s2):
        if x1 + s1 - 1 < x2 or y1 + s1 - 1 < y2 or x2 + s2 - 1 < x1 or (y2 + s2 - 1 < y1):
            return True
        else:
            return False

    def nextPos(self, placement, n, m, size):
        if not placement:
            return (0, 0)
        for i in range(n - size + 1):
            for j in range(m - size + 1):
                if all((self.hasNoOverLap(i, j, size, x, y, z) for (x, y, z) in placement)):
                    return (i, j)
        return (-1, -1)

    def canPlace(self, sizes, n, m, placement, memo):
        if len(sizes) == 0:
            return True
        h = tuple(placement)
        if h in memo:
            return memo[h]
        for (k, s) in enumerate(sizes):
            (i, j) = self.nextPos(placement, n, m, s)
            if i == -1:
                continue
            placement.append((i, j, s))
            if self.canPlace(sizes[:k] + sizes[k + 1:], n, m, placement, memo):
                memo[h] = True
                return True
            placement.pop()
        memo[h] = False
        return False

    def tilingRectangle(self, n: int, m: int) -> int:
        if n % m == 0:
            return n // m
        if m % n == 0:
            return m // n
        for i in range(3, 10):
            res = self.findSum(n, m, i)
            if any((self.canPlace(sizes, n, m, [], {}) for sizes in res)):
                return i

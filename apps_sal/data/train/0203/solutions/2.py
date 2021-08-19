class Solution:

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        counts = {}
        counts[1, 1] = 1
        for r in range(2, m + 1):
            counts[r, 1] = 1
        for c in range(2, n + 1):
            counts[1, c] = 1
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                counts[i, j] = counts[i - 1, j] + counts[i, j - 1]
        return counts[m, n]

    def temp(self, m, n):
        cache = {}

        def go(m, n):
            if m == 1 and n == 1:
                return 1
            count = 0
            if m > 1:
                if (m - 1, n) not in cache:
                    cache[m - 1, n] = go(m - 1, n)
                count += cache[m - 1, n]
            if n > 1:
                if (m, n - 1) not in cache:
                    cache[m, n - 1] = go(m, n - 1)
                count += cache[m, n - 1]
            return count
        return go(m, n)

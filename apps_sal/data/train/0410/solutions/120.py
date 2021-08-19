class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        degree_cache = {}

        def find_degree(n, degree=0):
            if n == 1:
                return degree
            if n % 2 == 0:
                degree = find_degree(n // 2, degree + 1)
            else:
                degree = find_degree(n * 3 + 1, degree + 1)
            return degree
        d = {}
        for i in range(lo, hi + 1):
            d[i] = find_degree(i, 0)
        sd = sorted(d.items(), key=lambda x: (x[1], x[0]))
        return sd[k - 1][0]

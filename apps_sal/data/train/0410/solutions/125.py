class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        d = {}
        for n in range(lo, hi + 1):
            count = 0
            p = n
            while(n != 1):
                if n % 2 == 0:
                    n = n / 2
                    count = count + 1
                elif n % 2 == 1:
                    n = 3 * n + 1
                    count = count + 1
            d[p] = count
        return sorted(list(d.items()), key=lambda x: x[1])[k - 1][0]

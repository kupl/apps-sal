class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(n: int) -> int:
            step = 0
            while n > 1:
                step += 1
                if n % 2 == 0:
                    n = n / 2
                else:
                    n = 3 * n + 1
            return step
        interval = [i for i in range(lo, hi + 1)]
        pwr = [[j, power(j)] for j in range(lo, hi + 1)]
        pwr = sorted(pwr, key=lambda x: x[1])

        return (pwr[k - 1][0])

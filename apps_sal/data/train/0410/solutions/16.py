class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        def power(n):
            counter = 0
            while n != 1:
                counter += 1
                if n % 2 == 0:
                    n = n // 2
                else:
                    n = 3 * n + 1
            return counter
        key = [x for x in range(lo, hi + 1)]
        value = [power(x) for x in key]
        ans = list(zip(key, value))
        sorted_ans = sorted(ans, key=lambda t: t[1])
        return sorted_ans[k - 1][0]

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        res = []
        for n in range(lo, hi + 1):
            power = 0
            x = n
            while x >= 1:
                if x == 1:
                    memo[n] = power
                    break
                elif x in memo:
                    power += memo[x]
                    memo[n] = power
                    break
                elif x % 2 == 0:
                    x //= 2
                    power += 1
                elif x % 2 != 0:
                    x = 3 * x + 1
                    power += 1

        res = sorted(memo.items(), key=lambda kv: (kv[1], kv[0]))
        return res[k - 1][0]

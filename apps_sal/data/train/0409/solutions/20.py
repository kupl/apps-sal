class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if k == 1:
            temp = arr
        else:
            temp = arr + arr
        cum = [0] * (len(temp) + 1)
        for i in range(1, len(temp) + 1):
            cum[i] = cum[i - 1] + temp[i - 1]
        cur = 0
        res = 0
        for c in cum:
            cur = min(cur, c)
            res = max(res, c - cur)
        MOD = 10 ** 9 + 7
        if k == 1:
            return res % MOD
        s = sum(arr)
        if res > 2 * s > 0:
            return (res + (k - 2) * s) % MOD
        elif s > 0:
            return k * s % MOD
        else:
            return res % MOD

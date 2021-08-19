class Solution:

    def numSub(self, s: str) -> int:
        res = 0
        mod = pow(10, 9) + 7
        i = 0
        while i < len(s):
            cnt = 0
            while i < len(s) and s[i] == '1':
                cnt += 1
                i += 1
            i += 1
            res += cnt * (cnt + 1) // 2 % mod
        return res

class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        if K == 1:
            return 1
        r = K % 10
        if r not in [1, 3, 7, 9]:
            return -1
        s = 0

        def dfs(s):
            digits = str(s)
            if digits.count('1') == len(digits):
                return len(digits)
            for i in range(10):
                s0 = i * K + s
                if s0 % 10 == 1:
                    r = 1 + dfs(s0 // 10)
                    if r > 0:
                        return r
            return -1
        result = dfs(0)
        return result

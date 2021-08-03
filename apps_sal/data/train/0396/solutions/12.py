class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K == 1:
            return 1
        r = K % 10
        if r not in [1, 3, 7, 9]:
            return -1
        s = 0

        @lru_cache(None)
        def dfs(s):
            digits = str(s)
            if digits.count('1') == len(digits):
                return len(digits)
            result = 10 ** 9
            for i in range(10):
                s0 = i * K + s
                if s0 % 10 == 1:
                    result = min(result, 1 + dfs(s0 // 10))
            return result

        result = dfs(0)
        return result if result < 10 ** 9 else -1

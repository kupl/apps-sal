class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        import math

        if K % 2 == 0 or K % 5 == 0:
            return -1

        digit_count = int(math.log10(K)) + 1

        i = 1
        ans = 1

        while i <= K:
            if ans % K == 0:
                return i

            i += 1
            ans = 10 * ans + 1

        return -1

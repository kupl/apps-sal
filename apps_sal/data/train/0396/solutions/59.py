class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        i = 1
        num = 1
        if K % 2 == 0:
            return -1
        while i <= K:
            if num % K == 0:
                return i
            num = num * 10 + 1
            i += 1
        return -1

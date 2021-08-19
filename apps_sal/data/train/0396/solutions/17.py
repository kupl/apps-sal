class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        if K == 1:
            return 1
        if K % 2 == 0 or K % 5 == 0:
            return -1
        num = 1
        count = 1
        while True:
            if num % K == 0:
                return count
            else:
                num = 10 * num + 1
                count += 1
        return -1

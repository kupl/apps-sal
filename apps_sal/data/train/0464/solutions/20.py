class Solution:
    def minOperations(self, n: int) -> int:

        if n == 1:
            return 0

        low = 0
        hi = n - 1
        num_ops = 0
        while low < hi:
            min_num = (2 * low) + 1
            max_num = (2 * hi) + 1

            num_ops += (max_num - min_num) // 2

            low += 1
            hi -= 1

        return num_ops

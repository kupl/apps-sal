class Solution:

    def minOperations(self, nums: List[int]) -> int:

        def count_ops(x: int) -> int:
            if x == 0:
                return (0, 0)
            elif x == 1:
                return (1, 0)
            elif x % 2 == 0:
                (add, mul) = count_ops(x // 2)
                return (add, mul + 1)
            else:
                (add, mul) = count_ops(x - 1)
                return (add + 1, mul)
        count = maxmul = 0
        for i in nums:
            (add, mul) = count_ops(i)
            maxmul = max(maxmul, mul)
            count += add
        return count + maxmul

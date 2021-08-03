class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def get_counts(x):
            if x == 0:
                return 0, 0
            elif x % 2 == 0:
                add_count, mul_count = get_counts(x // 2)
                return add_count, mul_count + 1
            else:
                add_count, mul_count = get_counts(x - 1)
                return add_count + 1, mul_count
        add_count, mul_count = 0, 0
        for num in nums:
            ac, mc = get_counts(num)
            add_count += ac
            mul_count = max(mc, mul_count)
        return add_count + mul_count

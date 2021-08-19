class Solution:

    def minOperations(self, nums: List[int]) -> int:

        def iter_count(x):
            shift_count = sub_count = 0
            while x > 0:
                if x & 1:
                    x -= 1
                    sub_count += 1
                else:
                    x >>= 1
                    shift_count += 1
            return (shift_count, sub_count)
        max_shift_count = 0
        total_subs = 0
        for x in nums:
            (i, j) = iter_count(x)
            max_shift_count = max(max_shift_count, i)
            total_subs += j
        return max_shift_count + total_subs

class Solution:

    def minOperations(self, nums: List[int]) -> int:
        d = {}
        odd = 0
        mx_even = 0
        for (i, val) in enumerate(nums):
            even = 0
            while val:
                if val % 2 == 0:
                    while val > 0 and val % 2 == 0:
                        val = val // 2
                        even += 1
                else:
                    val -= 1
                    odd += 1
            mx_even = max(even, mx_even)
        return odd + mx_even

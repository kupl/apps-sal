class Solution:
    # Size: (i), where i is the first i numbers
    # Problem: f(i) := the maximum length of a subarray that ends with ith number, where the product of all the elements is positive
    #          g(i) := the maximum lenghth of a subarray that ends with ith number, where the product of all the elements is negative
    # Recursive Cases:
    # - Recursive Case 1: nums[i] = 0
    #                     f(i) = 0
    #                     g(i) = 0
    # - Recursive Case 2: nums[i] > 0
    #                     f(i) = f(i-1) + 1
    #                     g(i) = g(i-1) + 1
    # - Recursive Case 3: nums[i] < 0
    #                     f(i) = g(i-1)
    #                     g(i) = f(i-1)
    # Base Cases: i = 0
    #             f(i) = 0
    #             g(i) = 0
    # Bottom Up: there is potential to optimize the space complexity
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        dp_f = [-1] * (n + 1)
        dp_g = [-1] * (n + 1)

        dp_f[0] = 0
        dp_g[0] = 0

        for i in range(1, n + 1):
            if nums[i - 1] == 0:
                dp_f[i] = 0
                dp_g[i] = 0
            elif nums[i - 1] > 0:
                dp_f[i] = dp_f[i - 1] + 1
                dp_g[i] = dp_g[i - 1] + 1 if dp_g[i - 1] > 0 else 0
            else:
                dp_f[i] = dp_g[i - 1] + 1 if dp_g[i - 1] > 0 else 0
                dp_g[i] = dp_f[i - 1] + 1
        return max(dp_f)

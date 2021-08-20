class Solution:

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        if k > math.factorial(n):
            return None
        else:
            nums = [str(i) for i in range(1, n + 1)]
            ans = ''
            while k % math.factorial(len(nums)) != 0:
                i = math.ceil(k / math.factorial(len(nums) - 1))
                k %= math.factorial(len(nums) - 1)
                ans += nums[i - 1]
                nums.pop(i - 1)
            ans += ''.join(nums[::-1])
            return ans

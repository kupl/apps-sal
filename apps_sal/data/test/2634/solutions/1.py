class Solution:

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def mask(x):
            return 1 << x
        exp = 1 << len(nums)
        ans = []
        for count in range(exp):
            new = []
            i = 0
            while mask(i) <= count:
                if mask(i) & count:
                    new.append(nums[i])
                i += 1
            ans.append(new)
        return ans

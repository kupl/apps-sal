class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_good_idx = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_good_idx:
                last_good_idx = i
        return True if last_good_idx == 0 else False

    def canJump_DP(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        print(len(nums))
        a = []
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                a.insert(0, False)
            elif i + nums[i] >= len(nums) - 1:
                a.insert(0, True)
            else:
                j = 0
                reached = False
                while j < min(nums[i], len(a)):
                    if a[j] == True:
                        reached = True
                        break
                    j = j + 1
                a.insert(0, reached)

        return a[0]

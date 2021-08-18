class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total % k != 0:
            return False
        target = total / k

        used = [False] * len(nums)
        nums = sorted(nums)

        def check(nums, k, cur, pos):
            if k == 1:
                return True
            for i in range(pos, -1, -1):
                if not used[i]:
                    if nums[i] + cur < target:
                        used[i] = True
                        if check(nums, k, cur + nums[i], i - 1):
                            return True
                        used[i] = False
                    elif nums[i] + cur == target:
                        used[i] = True
                        if check(nums, k - 1, 0, len(nums) - 1):
                            return True
                        used[i] = False
            return False
        return check(nums, k, 0, len(nums) - 1)

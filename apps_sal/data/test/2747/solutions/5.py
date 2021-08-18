class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s, e = -1, -1
        l, u = 0, len(nums) - 1
        if not nums or target > nums[u] or target < nums[l]:
            return [s, e]
        m = int((l + u) / 2)
        while u >= l:
            if nums[m] > target:
                if m == u:
                    break
                u = m
                m = int((l + u) / 2)
            elif nums[m] < target:
                l = m
                if int((l + u) / 2) == l:
                    m = l + 1
                else:
                    m = int((l + u) / 2)
            else:
                s = e = m
                while 0 < s and nums[s - 1] == nums[s]:
                    s -= 1
                while e < len(nums) - 1 and nums[e + 1] == nums[e]:
                    e += 1
                break
        return [s, e]

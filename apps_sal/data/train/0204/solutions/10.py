class Solution:

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while high >= low:
            mid = high + low // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                print('comes here')
                print(high)
                print(mid)
                print(low)
                high = mid - 1
                print(high)
        return -1

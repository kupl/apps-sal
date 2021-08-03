class Solution:
    res = False

    def searchR(self, nums, target, start, end):
        if(start > end or self.res == True):
            return self.res
        else:
            mid = int((start + end) / 2)
            print("Mid index: %d, Mid val: %d, Target: %d" % (mid, nums[mid], target))
            if(nums[mid] == target):
                self.res = True
            elif(nums[start] <= nums[mid]):
                if(nums[mid] == nums[end]):
                    self.searchR(nums, target, start, mid - 1)
                    self.searchR(nums, target, mid + 1, end)
                elif (target >= nums[start] and target <= nums[mid]):
                    self.searchR(nums, target, start, mid - 1)
                else:
                    self.searchR(nums, target, mid + 1, end)
            else:
                print("Here")
                if (target >= nums[mid] and target <= nums[end]):
                    self.searchR(nums, target, mid + 1, end)
                else:
                    self.searchR(nums, target, start, mid - 1)
            return self.res

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        res = self.searchR(nums, target, 0, (len(nums) - 1))
        return res

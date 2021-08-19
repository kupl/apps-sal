# 3:56

class Solution:
    def find_endindex(self, nums, ind, target):
        start = ind
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] + nums[ind] > target:
                end = mid
            else:
                start = mid + 1

        if nums[start] + nums[ind] > target:
            start -= 1

        # if start >= ind:
        return 2**(start - ind)
        # else:
        #    return 0

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums2 = sorted(nums)
        result = 0
        if nums2[0] > target:
            return result

        for i in range(len(nums2)):
            if nums2[i] * 2 <= target:
                res = self.find_endindex(nums2, i, target)
                #print (i, res)
                result += res
            else:
                break

        return result % (10**9 + 7)

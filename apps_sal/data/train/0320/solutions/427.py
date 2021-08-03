class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flag = True
        count = 0
        while flag:
            flag = False
            for i in range(len(nums)):
                if nums[i] & 1:
                    nums[i] -= nums[i] & 1
                    count += 1
                if nums[i] > 0:
                    nums[i] >>= 1
                    flag = True

            if flag:
                count += 1
        return count

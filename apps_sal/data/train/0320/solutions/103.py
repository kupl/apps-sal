class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        max_val, max_index = -1, len(nums)
        for i in range(len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
                max_index = i

        while(max_val != 0):
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    cnt += 1
            max_val = nums[max_index]
            # print(nums, max_val)
            if max_val == 0:
                break
            for i in range(len(nums)):
                nums[i] = nums[i] // 2
            cnt += 1
            max_val = nums[max_index]
            # print(nums, max_val)
        return cnt

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        cnt = 0
        while True:
            for i in range(len(nums)):
                if nums[i] != 0:
                    if nums[i] & 1 != 0:
                        nums[i] -= 1
                        cnt += 1
                    nums[i] = nums[i] >> 1
            if sum(nums) == 0:
                return cnt
            cnt += 1
        return cnt

        '''
        
        step = 0
        
        while True:
            for i in range(len(nums)):
                if nums[i]%2 != 0:
                    nums[i] = nums[i] - 1
                    step += 1
                nums[i] = nums[i]//2
            if sum(nums) == 0:
                return step
            step += 1
        '''

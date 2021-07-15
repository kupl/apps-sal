class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ans_count = 0
        while True:
            zero_count = 0
            have_odd = False
            ## op1
            for idx in range(len(nums)):
                if nums[idx] % 2 != 0:
                    have_odd = True
                    ans_count += 1
                    nums[idx] -= 1
                if nums[idx] == 0:
                    zero_count += 1
            ## check if all zero(break)
            if zero_count == len(nums):
                break
            ## op2
            if not have_odd:
                ans_count += 1
                for idx in range(len(nums)):
                    nums[idx] //= 2
            #print(nums, ans_count, zero_count)

        return ans_count

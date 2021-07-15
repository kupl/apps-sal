class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        cnt = 0
        mod = 10**9 + 7

        if nums[-1] <= (target // 2):
            return (pow(2, len(nums), mod) - 1)
        
        end = len(nums) - 1
        while end >= 0 and nums[0] + nums[end] > target:
            end -= 1

        print (end)
        for start in range(len(nums)):
            while (start <= end) and (nums[start] + nums[end]) > target:
                end -= 1
            
            if start > end:
                break
            print((start, end))
            cnt += pow(2, (end-start), mod)
            cnt %= mod
        
        
        return cnt
        


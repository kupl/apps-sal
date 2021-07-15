class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def dfs(n):
            if(sum(nums) == 0):
                return n
            subs = 0
            zeros = 0
            for i in range(len(nums)):
                if(nums[i]%2):
                    nums[i]-=1
                    subs+=1
                if(nums[i]==0):
                    zeros += 1
                nums[i] /= 2
            if(zeros == len(nums)):
                return subs+n
            return dfs(1+subs+n)
        return dfs(0)

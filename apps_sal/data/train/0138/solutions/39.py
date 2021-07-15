class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def dfs(start):
            i = start
            if i >= len(nums):
                return 0
            ret = 0
            stack = []
            while i < len(nums):
                if nums[i] == 0:
                    break
                elif nums[i] < 0:
                    stack.append(i)
                i+=1
            if len(stack) % 2 == 0:
                ret = i - start
            else:
                ret = max(i-1-stack[0],stack[-1]-start)
            
            return max(ret,dfs(i+1))
        return dfs(0)
                    


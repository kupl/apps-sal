class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        s = []; i=0
        while i < (len(nums)):
            if nums[i] == 0:
                s.append(0)
                i+=1
            else:
                j = i;cnt = 0
                while j<len(nums) and nums[j] == 1:
                    cnt+=1
                    j+=1
                s.append(cnt)
                i = j
        # print(s)
        if s[0] == len(nums):
            return len(nums)-1
        maxYet = max(s[0],s[len(s)-1])
        for i in range(1,len(s)-1):
            if s[i] == 0:
                maxYet = max(maxYet, s[i-1]+s[i+1])
            else:
                maxYet = max(maxYet,s[i])
        return maxYet
            
                


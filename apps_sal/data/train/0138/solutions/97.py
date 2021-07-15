class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        hashmap={0:-1}
        totalN=0
        ans=0
        for i in range(0,len(nums)):
            if nums[i]<0:
                totalN+=1
            
            value=totalN%2
            if nums[i]==0:
                hashmap={0:i}
                
                totalN=0
                continue
            if value in hashmap:
                ans=max(ans,i-hashmap[value])
            else:
                hashmap[value]=i
        return ans          

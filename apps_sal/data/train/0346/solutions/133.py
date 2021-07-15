class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(k):
            num_odd=res=i=0
            for j,v in enumerate(nums):
                if v%2 !=0:
                    num_odd+=1
                while num_odd>k:
                    if nums[i]%2==1:
                        num_odd-=1
                    i+=1
                res+=j-i+1
            return res
        
        return at_most(k)-at_most(k-1)


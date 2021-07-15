class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def atmostK(K):
            res=0
            k=0
            count=collections.Counter()
            for i in range(len(nums)):
                if(nums[i]%2==1): 
                    count[1]+=1
                while(count[1]>K):
                    if(nums[k]%2==1):
                        count[1]-=1
                    k+=1
                res+=i-k+1
            return res
        
        return atmostK(k)-atmostK(k-1)


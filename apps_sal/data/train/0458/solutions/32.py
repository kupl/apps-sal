class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        target=sum(nums)%p
 
        if target:
            
            memo={0:-1}

            res=0
            n=len(nums)
            ct={n}
            for i,j in enumerate(nums):
                    res=(res+j)%p
                    check=(res-target)%p 
                    if check in memo:
                        ct.add(i-memo[(res-target)%p])

                    memo[res]=i


            return -1 if min(ct)==n else min(ct)

        
        else:
            return 0

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        odd,even,re,s=0,1,0,0
        for v in arr:
            s+=v
            if s%2==0:
                re+=odd
                even+=1
            else:
                re+=even
                odd+=1
        return re%1000000007


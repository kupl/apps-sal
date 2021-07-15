class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        ans=0
        count=[1]+[0]*K
        prefix=0
        
        for num in A:
            prefix=(prefix+num)%K
            ans+=count[prefix]
            count[prefix]+=1
        
        return ans

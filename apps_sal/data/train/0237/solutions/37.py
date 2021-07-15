class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        counter=collections.Counter({0:1})
        s=0
        c=0
        for a in A:
            s+=a
            c+=counter[s-S]
            counter[s]+=1
        return c

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        ans=flip=0
        N=len(A)
        hint=[0]*N
        for i,x in enumerate(A):
            flip^=hint[i]
            if x^flip==0:
                ans+=1
                if i+K>N: return -1
                flip^=1
                if i+K<N: hint[i+K]^=1
        return ans

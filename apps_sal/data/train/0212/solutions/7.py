class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A=sorted(A)
        res=dict()
        for idx, a in enumerate(A):
            if idx==0:
                res[a]=1
            else:
                res[a]=1
                for j in range(idx):
                    if (a%A[j]==0) and (a//A[j] in A):
                        res[a]+=res[A[j]]*res[a//A[j]]
        return sum(res.values())%(10**9+7)

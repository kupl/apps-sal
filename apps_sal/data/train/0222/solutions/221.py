class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        seen,n={},len(A)
        A_set=set(A)
        def find_lens(ind,prev,curr):
            if ind==n:
                return 0
            key=(prev,curr)
            if key in seen:
                return seen[key]
            ans=0
            if prev+curr in A_set:
                for i in range(ind,n):
                    if curr+prev==A[i]:
                        ans=max(ans,find_lens(i+1,curr,A[i])+1)
            seen[key]=ans
            return ans
        ans=0
        for i in range(n-3):
            for j in range(i+1,n-2):
                if A[i]+A[j] not in A_set: continue
                ans=max(ans,find_lens(j+1,A[i],A[j]))
        return ans+2 if ans!=0 else 0

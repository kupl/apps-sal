class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index = {i:k for k,i in enumerate(A)}
        longest = collections.defaultdict(lambda:2) # ???
        
        ans = 0
        for k,z in enumerate(A):
            for j in range(k):
                i = index.get(z-A[j],None)  # index of z-A[j]
                if i is not None and i<j:
                    longest[j,k] = longest[i,j]+1
                    ans = max(ans, longest[j,k])
        return ans

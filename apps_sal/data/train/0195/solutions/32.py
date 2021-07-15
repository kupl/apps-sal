class Solution:
    def countTriplets(self, A: List[int]) -> int:
        N = len(A)
        ans = 0
        count = collections.Counter()
        for i in range(N):
            for j in range(N):
                count[A[i] & A[j]] += 1
        for k in range(N):
            for v in count:
                if A[k] & v == 0:
                    ans += count[v]
        
        return ans

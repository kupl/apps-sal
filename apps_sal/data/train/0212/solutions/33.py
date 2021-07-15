class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A = sorted(A)
        N = len(A)
        dp = [1 for _ in range(N)]
        index_map = {}
        for index in range(N):
            index_map[A[index]] = index
        
        for k in range(N):
            for i in range(k):
                if A[k] % A[i] == 0:
                    num_to_look = A[k]//A[i]
                    if num_to_look in index_map:
                        j = index_map[num_to_look]
                        dp[k] += dp[i]*dp[j] # okay why is this not giving me the right number?
         
        return sum(dp) % (10**9 +7)

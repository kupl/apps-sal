class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = [collections.defaultdict(int) for _ in range(len(A))]
        
        longest_seq = 0
        s = set(A)
        for i in range(2, len(A)):
            for j in range(i):
                if A[i] - A[j] in s and A[i] - A[j] < A[j]:
                    two_ago = A[i] - A[j]
                    one_ago = A[j]
                    if dp[j][two_ago] > 0:
                        dp[i][one_ago] = dp[j][two_ago] + 1
                    else:
                        dp[i][one_ago] = 3
                            
                    longest_seq = max(longest_seq, dp[i][one_ago])
                    
        return longest_seq


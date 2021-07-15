from heapq import heappop, heapify


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        # KEEP TRACK OF THE MAXIMUM COUNT
        count = 0
        
        # dp[i][d] = Length of arithmetic subsequence ending at A[i] (inclusive), with diff = d
        dp = defaultdict(lambda: defaultdict(int))
        
        for i in range(1, len(A)):
            seen = set()
            for j in range(i - 1, -1, -1):
                diff = A[i] - A[j]
                if diff not in seen:
                    dp[i][diff] += dp[j][diff] + 1
                    count = max(count, dp[i][diff])
                    seen.add(diff)
                    
        # for k, v in dp.items():
        #     print(k, v)
                                  
        return count + 1


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # O(NK) coming sooooon

        N = len(arr)
        dp = [0 for _ in range(N)] 

        dp[0] = arr[0]
        max_so_far = arr[0]
        for i in range(1, k):
            max_so_far = max(max_so_far, arr[i])
            dp[i] = (i+1) * max_so_far
        
        # now the actual thing
        for i in range(k, N):
            max_so_far = -sys.maxsize

            for j in range(i, i-k, -1):
                max_so_far = max(max_so_far, arr[j])
                dp[i] = max(dp[i], dp[j-1] + (i-j+1) * max_so_far)
        
        return dp[N-1]



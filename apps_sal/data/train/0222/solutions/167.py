class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:

        if(len(A) == 0):
            return 0
        mem = {}
        dp = [[-1 for x in range(len(A))] for y in range(len(A))]
        for idx, a in enumerate(A):
            mem[a] = idx
        max_l = 1
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                max_l = max(2 + self.get_valid_pibo(i, j, dp, A, mem), max_l)

        if(max_l == 2):
            max_l = 0
        return max_l

    def get_valid_pibo(self, i, j, dp, A, mem):
        if(dp[i][j] == -1):
            next_val = A[i] + A[j]
            if(next_val in mem):
                length = 1 + self.get_valid_pibo(j, mem[next_val], dp, A, mem)
                dp[i][j] = length
            else:
                length = 0
                dp[i][j] = 0
        return dp[i][j]

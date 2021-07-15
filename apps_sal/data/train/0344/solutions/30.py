class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        word_length = len(A[0])
        dp = [1] * word_length
        
        for index in range(word_length):
            for curr in range(index - 1, -1, -1):
                poss = True
                for k in range(len(A)):
                    if A[k][index] < A[k][curr]:
                        poss = False
                        break
                if poss:
                    dp[index] = max(dp[index], 1 + dp[curr])
        return word_length - max(dp)

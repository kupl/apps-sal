class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        ''' 
        S: d[i] be the answer for A[0]...A[i] answer = max sum of given array after partition. 
        R: want maximum of elements within K away from i. from hint 2:
        d[i] = d[i-j] + max{A[i-j],..., A[i]}*j, for j between 1 and k. 
        B = d[0]

        '''

        dp = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            temp = []
            for j in range(1, K + 1):
                if i - j >= 0:
                    k = dp[i - j] + max(A[i - j:i]) * j
                    temp.append(k)

            dp[i] = max(temp)
        return dp[len(A)]

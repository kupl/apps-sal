class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        # don't really understand question. how did they partition exactly????

        # dynamic programming!
        # let d[i] be the answer for A[0]...A[i-1]
        ''' 
        S: d[i] be the answer for A[0]...A[i] answer = max sum of given array after partition. 
        R: want maximum of elements within K away from i. from hint 2:
        d[i] = d[i-j] + max{A[i-j],..., A[i]}*j, for j between 1 and k. 
        #times j because the max of that partition becomes the corresponding max for all            the positions in transformed A. 
        B = d[0]

        '''
        # base case:

        # reference: https://leetcode.com/problems/partition-array-for-maximum-sum/discuss/783353/dp-with-python-and-some-comments-of-idea
        dp = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            temp = []
            for j in range(1, K + 1):  # go through all possible values of j
                if i - j >= 0:
                    k = dp[i - j] + max(A[i - j:i]) * j
                    temp.append(k)
                    # print(k)
                    # dp[i] = max(k, dp[i])
                    # storing stuff in the same index so replacing it every time.

            dp[i] = max(temp)
        return dp[len(A)]

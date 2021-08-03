class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        '''
        Subarray sum = k problem
        '''

        cur = 0
        res = 0
        dp = collections.defaultdict(int)
        dp[0] = 1
        for i in range(len(A)):
            cur += A[i]
            diff = cur - S
            if diff in dp:
                res += dp[diff]
            dp[cur] += 1

        return res

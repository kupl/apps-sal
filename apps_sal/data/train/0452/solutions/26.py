class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        '''
        max_d(i,i+k-1) = 

        dp(i, d_left) = 
        if d_left == 0: 
            return float('inf')
        if i == len(jobDifficulty)-1:
            if d_left > 1:
                return float('inf')
            else:
                return jobDifficulty[i]

        for k in range(1, len(jobDifficulty)-i):
            res = min(res, dp(i+k, d_left-1) + max_d(i,i+k-1))


        jobDifficulty = [6,5,4,3,2,1], d = 2
        '''
        max_d = [[-1 for _ in range(len(jobDifficulty))] for _ in range(len(jobDifficulty))]
        for i in range(len(jobDifficulty)):
            max_d[i][i] = jobDifficulty[i]
            for j in range(i + 1, len(jobDifficulty)):
                max_d[i][j] = max(jobDifficulty[j], max_d[i][j - 1])

        def dp(i, d_left):
            if d_left == 0:
                return float('inf')
            if d_left == 1:
                return max_d[i][-1]
            if i == len(jobDifficulty) - 1:
                if d_left > 1:
                    return float('inf')
                else:
                    return jobDifficulty[i]
            if (i, d_left) in memo.keys():
                return memo[(i, d_left)]
            res = float('inf')
            for k in range(1, len(jobDifficulty) - i):
                res = min(res, dp(i + k, d_left - 1) + max_d[i][i + k - 1])

            memo[(i, d_left)] = res
            return res
        memo = {}

        ans = dp(0, d)
        # print(max_d)
        # print(memo)
        return ans if ans != float('inf') else -1

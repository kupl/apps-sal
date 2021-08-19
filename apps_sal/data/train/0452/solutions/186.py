class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        n = len(jobDifficulty)
        if n < d:
            return -1
        memo = {}

        def dp(ii, day):
            if (ii, day) not in memo:
                if n - ii == day:
                    memo[(ii, day)] = sum(jobDifficulty[ii:])
                elif day == 1:
                    memo[(ii, day)] = max(jobDifficulty[ii:])
                else:
                    ans = float('inf')
                    curr_max = float('-inf')
                    for jj in range(ii, n - (day - 1)):
                        #print(jj, day)
                        curr_max = max(curr_max, jobDifficulty[jj])
                        ans = min(ans, curr_max + dp(jj + 1, day - 1))

                    memo[(ii, day)] = ans
            return memo[(ii, day)]

        ans = dp(0, d)
        # print(memo)
        return ans

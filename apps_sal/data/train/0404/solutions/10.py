class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        s, dp = [0] + A, {}
        for i in range(1, len(A) + 1):
            s[i] += s[i - 1]
        # print(s)

        def dfs(i, k):
            #print(i, k)
            if k == 1:
                #print((s[-1] - s[i]) / (len(A) - i))
                return (s[-1] - s[i]) / (len(A) - i)
            if (i, k) in dp:
                return dp[(i, k)]
            dp[(i, k)] = max((s[j] - s[i]) / (j - i) + dfs(j, k - 1) for j in range(i + 1, len(A) - k + 2))
            return dp[(i, k)]
        return dfs(0, K)

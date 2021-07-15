class Solution:
    def cal(self, i, j, cuts):
        if i in self.dp:
            if j in self.dp[i]:
                return self.dp[i][j]
        ans = float('inf')
        cost = j - i
        found = False
        for ind, c in enumerate(cuts):
            if i < c and c < j:
                t = cuts[:]
                del t[ind]
                ans = min(ans, cost + self.cal(i, c, t) + self.cal(c, j, t))
                found = True
        if not found:
            ans = 0
        if i in self.dp:
            self.dp[i][j] = ans
        else:
            self.dp[i] = {j: ans}
        return ans
    
    def minCost(self, n: int, cuts: List[int]) -> int:
        self.dp = {}
        return self.cal(0, n, sorted(cuts))

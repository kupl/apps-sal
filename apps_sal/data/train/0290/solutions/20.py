class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        return self.dp(0, n, cuts, dict())
    
    def dp(self, i, j, cuts, memo):
        if (i, j) not in memo:
            minV = float('inf')
            for k in cuts:
                if k > i and k < j: # Valid cutting point
                    l, r = self.dp(i, k, cuts, memo), self.dp(k, j, cuts, memo)
                    minV = min(minV, l+r)
            if minV != float('inf'):
                memo[(i, j)] = minV+j-i
            else:
                memo[(i, j)] = 0
        return memo[(i, j)]

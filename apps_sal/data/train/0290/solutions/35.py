class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = {}
        def minCostij(i, j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i + 1 == j or i == j:
                dp[(i,j)] = 0
            else:
                minCosts = [minCostij(i,k) + minCostij(k,j) for k in cuts if (k < j and k > i)]
                if minCosts:
                    dp[(i,j)] = min(minCosts) + (j-i)
                else:
                    dp[(i,j)] = 0
            return dp[(i,j)]
        return minCostij(0,n)


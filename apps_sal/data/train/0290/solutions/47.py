class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # cuts.append(0)
        # cuts.append(n)
        # cuts.sort()
        return self.dp(cuts, 0, n, dict())
    
    def dp(self, cuts, a, b, memo):
        if (a, b) not in memo:
            memo[(a, b)], minV = float('inf'),float('inf')
            for j, c in enumerate(cuts):
                if c > a and c < b:
                    l, r = self.dp(cuts, a,c,memo), self.dp(cuts, c,b,memo)
                    memo[(a, b)] = min(memo[(a, b)], b-a)
                    minV = min(minV, l+r)
            if memo[(a, b)] == float('inf'):
                memo[(a, b)] = 0
            else:
                memo[(a, b)] += minV
        return memo[(a, b)]

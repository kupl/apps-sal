MOD = int(10**9 + 7)

class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        n = len(group)
        dp = (128*101)*[0]
        dp[0] = 1
        for g,p in zip(group,profit):
            old = dp.copy()
            for h in range(0,G-g+1):
                for q in range(P+1):
                    x = (h+g)<<7 | min(p+q,P)
                    y = dp[x]
                    y += old[h<<7 | q]
                    if y > MOD:
                        y -= MOD
                    dp[x] = y
            #print(*[(i,x) for i,x in enumerate(dp) if x])
        return sum(dp[g<<7 | P] for g in range(G+1)) % MOD

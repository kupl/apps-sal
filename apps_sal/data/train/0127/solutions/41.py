class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        mod = 10**9 + 7        
        DP = [[[0] * (P+1) for _ in range(G+1)] for _ in range(len(group)+1)]
        DP[0][0][0] = 1
        
        for k in range(1, len(group)+1):
            g = group[k-1]
            p = profit[k-1]
            for i in range(G+1):
                for j in range(P+1):
                    DP[k][i][j] = DP[k-1][i][j]
                    if i-g < 0:
                        continue
                    DP[k][i][j] = DP[k-1][i][j] + DP[k-1][i-g][max(0, j-p)]
        ans = 0
        for i in range(G+1):
            ans += DP[len(group)][i][P]%mod
        return ans%mod
        '''
        m = {}
        mod = 10**9 + 7
        def dfs(idx, g, p):
            if idx == 0:
                if (idx, g, p) == (0, 0, 0):
                    return 1
                return 0
            #if g <= 0:
            #    return 0
            if (idx, g, p) in m:
                return m[(idx, g, p)]
            res = 0
            res = (dfs(idx-1, g, p) + dfs(idx-1, g-group[idx-1], max(0, p-profit[idx-1])))%mod
            m[(idx, g, p)] = res
            return res
        ans = 0
        for i in range(G+1):
            ans += dfs(len(group), i, P)%mod
        return ans%mod
        '''
        '''
        m = {}
        
        def dfs(idx, g, p):
            res = 0
            if idx == 0:
                if g >= group[0] and profit[0] >= p:
                    res = 1
                return res
            if g <=0:
                return 0
            if p == 0:
                
            if (idx, g, p) in m:
                return m[(idx, g, p)]
            
            res = m[(idx-1, g, p)] + dfs(idx-1, g-group[idx], max(0, p-profit[idx]))
            m[(idx, g, p)] = res
            return res
        '''

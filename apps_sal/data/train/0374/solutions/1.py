class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        N = len(A)
        def Cost(x, y):
            cost = len(y)
            max_similarity = 0
            for i in range(1, min(len(x), len(y))):
                if x[-i:] == y[:i]: max_similarity = i
            return cost - max_similarity
            
        g = [[float('inf')] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i != j:
                    cost = Cost(A[i], A[j])
                    g[i][j] = cost
                else: g[i][j] = len(A[i])
                    
        dp = [[float('inf')] * N for _ in range(1<<N)]
        parent = [[-1] * N for _ in range(1<<N)]
        
        for i in range(N):
            dp[1<<i][i] = len(A[i])
        
        for s in range(1, 1<<N):
            for i in range(N):
                if s & (1<<i):  #valid dp[s][i] check
                    prev = s - (1<<i)
                    for j in range(N):
                        if j != i and prev & (1<<j):
                            cur_cost = dp[prev][j] + g[j][i]
                            if cur_cost < dp[s][i]:
                                dp[s][i] = cur_cost
                                parent[s][i] = j
                                
        min_cost = float('inf')
        ind = -1
        last_row = dp[2**N - 1]
        for i in range(N):
            if last_row[i] < min_cost:
                min_cost = last_row[i]
                ind = i
        
        s = 2**N - 1
        res = A[ind]
        child_ind = ind
        # print(s, ind)
        ind = parent[s][ind]
        s = s - (1<<child_ind)
        while s and ind >= 0:
            cost = g[ind][child_ind]
            pre_len = len(A[ind]) - len(A[child_ind]) + g[ind][child_ind]
            res = A[ind][:pre_len] + res
            child_ind = ind
            # print(s, ind)
            ind = parent[s][ind]
            s = s - (1<<child_ind)
            
        return res
            
                
                
                            
                    
            


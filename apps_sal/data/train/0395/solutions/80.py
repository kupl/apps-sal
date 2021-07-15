class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)
        
        # preparation: sorted A
        aS = [(val, i) for i, val in enumerate(A)]
        aS.sort(key=lambda x: x[0])
        a_map = {}
        for id, (val, i) in enumerate(aS):
            a_map[i] = id
        dS = [(val, i) for i, val in enumerate(A)]
        dS.sort(key=lambda x: x[0], reverse=True)
        d_map = {}
        for id, (val, i) in enumerate(dS):
            d_map[i] = id
                
        # dp[i] tracks the validness for tarting index i, dp[i] = [x, y] where x, y = 1/0 indicating an (x) even jump or an (y) odd being valid or not
        dp = [[0,0]] * N
        dp[N - 1] = [1, 1]
        
        for i in range(N - 2, -1, -1):
            dp[i] = [0, 0]
            # even jump, find the biggest smaller one next
            id = d_map[i]
            while id + 1 < N: 
                val, j = dS[id + 1]
                if j > i: 
                    dp[i][0] = dp[j][1]
                    break
                id = id + 1
            # odd jump, find the smallest bigger one next
            id = a_map[i]
            while id + 1 < N: 
                val, j = aS[id + 1]
                if j > i: 
                    dp[i][1] = dp[j][0]
                    break
                id = id + 1
        
        # find the dp[i] with odd (1st) is 1
        cnt = 0
        for i in range(N):
            cnt += dp[i][1]
        
        return cnt
            
                    
            
        


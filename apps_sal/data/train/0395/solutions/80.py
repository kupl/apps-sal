class Solution:

    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)
        aS = [(val, i) for (i, val) in enumerate(A)]
        aS.sort(key=lambda x: x[0])
        a_map = {}
        for (id, (val, i)) in enumerate(aS):
            a_map[i] = id
        dS = [(val, i) for (i, val) in enumerate(A)]
        dS.sort(key=lambda x: x[0], reverse=True)
        d_map = {}
        for (id, (val, i)) in enumerate(dS):
            d_map[i] = id
        dp = [[0, 0]] * N
        dp[N - 1] = [1, 1]
        for i in range(N - 2, -1, -1):
            dp[i] = [0, 0]
            id = d_map[i]
            while id + 1 < N:
                (val, j) = dS[id + 1]
                if j > i:
                    dp[i][0] = dp[j][1]
                    break
                id = id + 1
            id = a_map[i]
            while id + 1 < N:
                (val, j) = aS[id + 1]
                if j > i:
                    dp[i][1] = dp[j][0]
                    break
                id = id + 1
        cnt = 0
        for i in range(N):
            cnt += dp[i][1]
        return cnt

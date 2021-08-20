class Solution:

    def shortestSuperstring(self, A: List[str]) -> str:
        N = len(A)
        cost = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                cost[i][j] = math.inf
                for k in range(len(A[i])):
                    if A[j].startswith(A[i][k:]):
                        cost[i][j] = k + len(A[j]) - len(A[i])
                        break
                if cost[i][j] == math.inf:
                    cost[i][j] = len(A[j])
        dp = [[math.inf for _ in range(1 << N)] for i in range(N)]
        for i in range(N):
            dp[i][1 << i] = len(A[i])
        backtrack = [[None] * (1 << N) for _ in range(N)]
        for i in range(N):
            backtrack[i][1 << i] = (i, 0)
        for i in range(1 << N):
            for j in range(N):
                if i & 1 << j:
                    for k in range(N):
                        if i & 1 << k and i != k:
                            if dp[j][i] > dp[k][i ^ 1 << j] + cost[k][j]:
                                dp[j][i] = dp[k][i ^ 1 << j] + cost[k][j]
                                backtrack[j][i] = (k, i ^ 1 << j)
        min_cost = math.inf
        min_index = -1
        for i in range(N):
            if min_cost > dp[i][(1 << N) - 1]:
                min_cost = dp[i][(1 << N) - 1]
                min_index = i
        mask = (1 << N) - 1
        order = []
        while mask:
            order.append(min_index)
            (min_index, mask) = backtrack[min_index][mask]
        order.reverse()
        answer = []
        last_i = -1
        for i in order:
            if len(answer) == 0:
                answer.append(A[i])
            else:
                answer.append(A[i][-cost[last_i][i]:])
            last_i = i
        return ''.join(answer)

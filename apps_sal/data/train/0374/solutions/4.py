class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        size = len(A)
        costs = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if i == j:
                    costs[i][j] = 0
                    continue
                wi, wj = A[i], A[j]
                si, sj = len(wi), len(wj)
                costs[i][j] = sj
                for k in range(1, min(si, sj) + 1):
                    if wi[-k:] == wj[:k]:
                        costs[i][j] = sj - k
        dp = [[20 * 12] * size for _ in range(1 << size)]
        parent = [[-1] * size for _ in range(1 << size)]
        for i in range(size):
            dp[1 << i][i] = len(A[i])
        for state in range(1, 1 << size):
            for i in range(size):
                if state & (1 << i) == 0:
                    continue
                prev = state - (1 << i)
                for j in range(size):
                    if prev & (1 << j) == 0:
                        continue
                    if dp[state][i] > dp[prev][j] + costs[j][i]:
                        dp[state][i] = dp[prev][j] + costs[j][i]
                        parent[state][i] = j
        minCost = min(dp[-1])
        index = dp[-1].index(minCost)
        res = ''
        state = (1 << size) - 1
        while state:
            prevIndex = parent[state][index]
            if prevIndex < 0:
                res = A[index] + res
            else:
                cost = costs[prevIndex][index]
                res = A[index][-cost:] + res
            state -= 1 << index
            index = prevIndex
        return res

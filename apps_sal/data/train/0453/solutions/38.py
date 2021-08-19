dp = [[[0] * 102 for j in range(23)] for i in range(102)]


def dfs(i, house, cost, prev, tar):
    if i >= len(house):
        if tar == 0:
            return 0
        else:
            return 1000000000000
    if tar < 0:
        return 1000000000000
    if(dp[i][prev][tar] > 0):
        return dp[i][prev][tar]
    res = 1000000000000000000
    if house[i] == 0:
        for j in range(len(cost[i])):
            res = min(res, cost[i][j] + dfs(i + 1, house, cost, j + 1, tar - ((j + 1) != prev)))
    else:
        res = min(res, dfs(i + 1, house, cost, house[i], tar - (house[i] != prev)))
    # print(i,prev,tar,res)
    dp[i][prev][tar] = res
    return dp[i][prev][tar]


class Solution:
    def minCost(self, house: List[int], cost: List[List[int]], m: int, n: int, tar: int) -> int:
        for i in range(101):
            for j in range(21):
                for k in range(101):
                    dp[i][j][k] = 0
        res = dfs(0, house, cost, n + 1, tar)
        # for i in dp:
        #    print(i)
        if res >= 1000000000000:
            return -1
        else:
            return res

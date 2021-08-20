class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        if n == 1 and target >= 2:
            return -1
        if target > m:
            return -1
        c = 0
        p = -1
        for i in range(m):
            if houses[i] > 0 and houses[i] != p:
                c += 1
                p = houses[i]
        if c > target:
            return -1
        cache = {}
        MAX_VAL = float('inf')

        def process(i, p, t):
            if t < 0:
                return MAX_VAL
            if i == m:
                if t == 0:
                    return 0
                else:
                    return MAX_VAL
            elif not (i, p, t) in cache:
                ans = MAX_VAL
                if houses[i] > 0:
                    if houses[i] == p:
                        ans = process(i + 1, p, t)
                    else:
                        ans = process(i + 1, houses[i], t - 1)
                else:
                    ans = MAX_VAL
                    for j in range(n):
                        if p == j + 1:
                            ans = min(ans, cost[i][j] + process(i + 1, p, t))
                        else:
                            ans = min(ans, cost[i][j] + process(i + 1, j + 1, t - 1))
                cache[i, p, t] = ans
            return cache[i, p, t]
        x = process(0, -1, target)
        return x if x != MAX_VAL else -1

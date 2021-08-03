class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        s = list(s)
        min_cost = 0
        cur = []
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                cur.append(i)
            else:
                if len(cur) > 0:
                    cur.append(i)
                    min_cost += sum([cost[x] for x in cur]) - max(
                        [cost[x] for x in cur])
                    cur = []
        if len(cur) > 0:
            cur.append(len(s) - 1)
            min_cost += sum([cost[x] for x in cur]) - max(
                [cost[x] for x in cur])
        return min_cost

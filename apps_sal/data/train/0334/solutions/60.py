class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        target = s[0]
        track_max = cost[0]
        curr_sum = cost[0]
        res = 0
        for i in range(1, len(cost)):
            if s[i] == target:
                track_max = max(track_max, cost[i])
                curr_sum += cost[i]
            else:
                if curr_sum != cost[i - 1]:
                    res += curr_sum - track_max
                track_max = cost[i]
                curr_sum = cost[i]
                target = s[i]
        if curr_sum != cost[i - 1]:
            res += curr_sum - track_max
        return res

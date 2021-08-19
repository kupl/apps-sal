class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        length = 1
        (start, end) = (0, 0)
        result = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                if length == 1:
                    start = i
                length += 1
            else:
                if length > 1:
                    end = i
                    sm = sum(cost[start:end + 1])
                    mx = max(cost[start:end + 1])
                    result += sm - mx
                start = 0
                end = 0
                length = 1
        if length > 1:
            end = len(s) - 1
            sm = sum(cost[start:end + 1])
            mx = max(cost[start:end + 1])
            result += sm - mx
        return result

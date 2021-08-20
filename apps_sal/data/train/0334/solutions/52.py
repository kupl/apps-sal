class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        repeats = []
        low = 0
        high = 0
        for i in range(1, len(s)):
            if s[i] == s[low]:
                high = i
            else:
                if high - low > 0:
                    repeats.append((low, high + 1))
                low = high = i
        if high - low > 0:
            repeats.append((low, high + 1))
        total = 0
        for (low, high) in repeats:
            maxVal = 0
            for i in range(low, high):
                maxVal = max(maxVal, cost[i])
                total = total + cost[i]
            total = total - maxVal
        return total

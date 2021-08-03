class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        result = 0
        low = 0

        while low < len(cost) - 1:
            high = low + 1
            while high < len(cost) and s[high] == s[low]:
                high += 1

            if high - low > 1:
                a, ma = 0, float('-inf')
                for i in range(low, high):
                    a += cost[i]
                    ma = max(ma, cost[i])
                result += a - ma
            low = high
        return result

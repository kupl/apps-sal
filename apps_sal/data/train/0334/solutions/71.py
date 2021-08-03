class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        minCost = 0

        left = right = 0
        while right < n:
            while right < n and s[right] == s[left]:
                right += 1

            if right == left + 1:
                left += 1
            else:
                minCost += sum(cost[left:right]) - max(cost[left:right])
                left = right

        return minCost

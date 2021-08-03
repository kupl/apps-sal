class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        last_char = ''
        start = 0
        ans = 0
        s += '_'
        cost.append(0)

        for i, c in enumerate(s):

            if c != last_char:
                if i - start > 1:
                    ans += sum(cost[start: i]) - max(cost[start: i])
                last_char = c
                start = i

        return ans

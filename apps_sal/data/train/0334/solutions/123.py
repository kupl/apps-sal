class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)

        def getnextidx(k):
            for l in range(k + 1, n):
                if s[k] != s[l]:
                    return l
            return n
        i = 0
        cost_used = 0
        while i < n:
            j = getnextidx(i)
            if j - i > 1:
                cost_used += sum(cost[i:j]) - max(cost[i:j])
            i = j
        return cost_used

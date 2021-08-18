class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:

        def getNextIdx(idx):
            curr = s[idx]
            for j, ch in enumerate(s[idx + 1:]):
                if ch != curr:
                    return j + idx + 1
            return len(s)

        i = 0

        sol = 0

        while i < len(s):
            next_i = getNextIdx(i)
            if i < len(s) - 1 and s[i] != s[i + 1]:
                i += 1
            else:
                curr = s[i]
                max_cost_idx = i
                for xx in range(i + 1, min(next_i, len(s))):
                    if cost[xx] > cost[max_cost_idx]:
                        max_cost_idx = xx
                for idx in range(i, min(next_i, len(s))):
                    if idx != max_cost_idx:
                        sol += cost[idx]
                i = next_i
        return sol

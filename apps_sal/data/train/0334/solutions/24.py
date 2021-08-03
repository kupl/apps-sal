class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if len(s) == 1:
            return 0
        total = 0
        s = list(s)
        l, r = 0, 1
        while r < len(s):
            if s[l] == '':
                l += 1
            else:
                if s[l] == s[r]:
                    if cost[l] > cost[r]:
                        total += cost[r]
                        s[r] = ''
                        r += 1

                    else:
                        total += cost[l]
                        l = r
                        r += 1
                else:
                    l += 1
                    r += 1
        return total

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        c = 0
        i = 0
        l = len(cost)
        while i < l - 1:
            if s[i] != s[i + 1]:
                i = i + 1
            else:
                ch = s[i]
                dl = 0
                for char in s[i:]:
                    if char == ch:
                        dl += 1
                    else:
                        break
                m = cost[i:i + dl]
                print(m)
                c += sum(m) - max(m)
                i += dl
        return c

class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        s = list(s)
        c = 0
        i = 0
        while i < len(s) - 1:
            st = 0
            end = 0
            if s[i] == s[i + 1]:
                st = i
                while i < len(s) - 1 and s[i] == s[i + 1]:
                    end = i + 1
                    i += 1
                print((st, end))
                c += sum(cost[st:end + 1]) - max(cost[st:end + 1])
                print(c)
            else:
                i += 1
        return c

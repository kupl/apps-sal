class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        arr = []
        i = 1
        while i < len(s):
            temp = set()
            if s[i] == s[i - 1]:
                while i < len(s) and s[i] == s[i - 1]:
                    temp.add(i - 1)
                    temp.add(i)
                    i += 1
                arr += [list(temp)]
            else:
                i += 1
        c = 0
        for i in arr:
            temp = [cost[x] for x in i]
            c += sum(temp) - max(temp)
        return c

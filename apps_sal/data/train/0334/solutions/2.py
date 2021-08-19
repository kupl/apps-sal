class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        val = 0
        i = 0
        start = 0
        while i + 1 < len(s):
            if s[i] == s[i + 1]:
                if start == 0:
                    temp = [(i, cost[i])]
                    start = 1
                else:
                    temp.append((i, cost[i]))
            elif start == 1:
                temp.append((i, cost[i]))
                start = 0
                temp = sorted(temp, key=lambda x: x[1])
                print(temp)
                val += sum([i[1] for i in temp[:-1]])
            i += 1
        if start == 1:
            temp.append((i, cost[i]))
            temp = sorted(temp, key=lambda x: x[1])
            val += sum([i[1] for i in temp[:-1]])
        return val

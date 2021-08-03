class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        temp = []
        t = []
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                t.append(i)
            while i < len(s) - 1 and s[i] == s[i + 1]:
                t.append(i + 1)
                i += 1
            if len(t) > 0:
                temp.append(t)
                t = []
            i += 1
        else:
            if len(t) > 0:
                temp.append(t)
                t = []
        print(temp)
        ans = 0
        for i in temp:
            tt = -max(cost[min(i):max(i) + 1])
            tt += sum(cost[min(i):max(i) + 1])
            ans += tt
        return ans

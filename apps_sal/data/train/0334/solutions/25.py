class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        tmp = []
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                tmp.append(i)
                tmp.append(i - 1)
            if s[i] != s[i - 1] or i == len(s) - 1:
                tmp = list(set(tmp))
                x = []
                for el in tmp:
                    x.append(cost[el])
                tmp = x
                tmp.sort()
                tmp = tmp[:-1]
                ans += sum(tmp)
                tmp = []

        return ans

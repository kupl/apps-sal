class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if len(s) == 1:
            return 0
        temp = []
        j = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                if s[i] == s[j]:
                    temp.append([j, i + 1])
                else:
                    if (i - j) > 1:
                        temp.append([j, i])
            else:
                if s[j] != s[i]:
                    if (i - j) > 1:
                        temp.append([j, i])
                    j = i
        res = 0
        for i, j in temp:
            new = cost[i:j]
            val = max(new)
            p = 0
            while p < len(new):
                if new[p] == val:
                    new.pop(p)
                    break
                p += 1
            res += sum(new)
        return res

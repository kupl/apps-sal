class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        ans = []
        i = 0
        while i < len(s):
            count = 0
            for j in range(i + 1, len(s)):
                if s[j] != s[i]:
                    break
                else:
                    count += 1
            if count > 0:
                ans.append((i, i + count))
            i = j
            if i == len(s) - 1:
                break
        res = 0
        i = (3, 5)
        for i in ans:
            k = sorted(cost[i[0]:i[1] + 1])
            res = res + sum(k[0:i[1] - i[0]])
        return res

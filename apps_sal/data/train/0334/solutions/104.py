class Solution:

    def minCost(self, s: str, cost: List[int]) -> int:
        to_delete = []
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1] or (i < len(s) - 1 and s[i] == s[i + 1]):
                to_delete.append(i)
        (groups, temp, prev) = ([], [], -1)
        for i in range(len(to_delete)):
            if prev == -1:
                prev = to_delete[i]
                temp.append(to_delete[i])
            elif i == len(to_delete) - 1:
                temp.append(to_delete[i])
                groups.append(temp[:])
            elif to_delete[i + 1] - to_delete[i] > 1 or s[to_delete[i + 1]] != s[to_delete[i]]:
                temp.append(to_delete[i])
                groups.append(temp[:])
                prev = -1
                temp = []
            else:
                temp.append(to_delete[i])
        ans = 0
        for group in groups:
            total = 0
            highest = 0
            for index in group:
                total += cost[index]
                highest = max(highest, cost[index])
            ans += total - highest
        return ans

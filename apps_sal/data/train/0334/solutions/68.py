class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        to_delete = []
        i = 0
        while i < len(s):
            j = i + 1
            flag = False
            while j < len(s) and s[j] == s[i]:
                j += 1
                flag = True
            if flag:
                to_delete.append((i, j))
            i = j
        ans = 0
        for interval in to_delete:
            cos = sorted(cost[interval[0]: interval[1]])
            l = interval[1] - interval[0] - 1
            index = 0
            for _ in range(l):
                ans += cos[index]
                index += 1
        return ans

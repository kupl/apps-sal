class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        i = 0
        delete = []
        while i < len(s) - 1:
            j = i + 1
            while j < len(s):
                if s[j] != s[i]:
                    break
                j += 1
            if j > i + 1:
                temp = [a for a in range(i, j)]
                temp2 = [x for _, x in sorted(zip(cost[i:j], temp))]
                delete += temp2[:-1]
            i = j
        delete = set(delete)
        res = 0
        for i, x in enumerate(cost):
            if i in delete:
                res += x
        return res

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] != s[i+1]:
                # print('-', s[i], i)
                i += 1
            elif i + 1 < len(s) and s[i] == s[i+1]:
                # print('+', s[i], i)
                j = i + 1
                while j + 1 < len(s) and s[j] == s[j+1]:
                    j += 1
                j += 1
                # print('+', i, j)
                summ = 0
                maxx = float('-inf')
                for k in range(i, j):
                    summ += cost[k]
                    maxx = max(maxx, cost[k])
                ans += (summ - maxx)
                i = j
            else:
                i += 1
        return ans
            
            


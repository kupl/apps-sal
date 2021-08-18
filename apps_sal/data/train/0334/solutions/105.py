class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        answer = 0
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                sumCost = cost[i]
                maxCost = cost[i]
                j = i + 1
                while(j < len(s) - 1 and s[j] == s[j + 1]):
                    sumCost += cost[j]
                    maxCost = max(maxCost, cost[j])
                    j += 1
                if s[j] == s[i]:
                    sumCost += cost[j]
                    maxCost = max(maxCost, cost[j])
                answer += sumCost - maxCost
                i = j + 1
            else:
                i += 1
        return answer

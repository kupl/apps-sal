class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        mcost = 0

        for i in range(0, len(s)-1):

            if s[i] == s[i+1]:

                if cost[i] < cost[i+1]:
                    mcost += cost[i]
                else:
                    mcost += cost[i+1]

                    #then swap the cost
                    temp = cost[i]
                    cost[i] = cost[i+1]
                    cost[i+1] = temp


        return mcost

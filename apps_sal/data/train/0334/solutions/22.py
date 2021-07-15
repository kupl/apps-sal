import heapq

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        it = 0
        n = len(s)
        ans = 0
        while it<n:
            if it>0 and s[it-1] == s[it]:
                h,c = [],s[it]
                heapq.heappush(h,cost[it])
                heapq.heappush(h,cost[it-1])
                it+=1
                while it<n and s[it]==c:
                    heapq.heappush(h,cost[it])
                    it+=1
                sze = len(h)
                ans += sum(heapq.nsmallest(sze-1,h))
            else:
                it+=1
                
        return ans 

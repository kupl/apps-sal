import heapq
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        i = 1
        h = []
        summ = 0
        while i < len(s):
            if(s[i]==s[i-1]):
                while(i<len(s) and s[i]==s[i-1]):
                    heapq.heappush(h,cost[i-1])
                    i+=1
                heapq.heappush(h,cost[i-1])
                while len(h)>1:
                    summ += heapq.heappop(h)
                heapq.heappop(h)
            else:
                i+=1
        return summ

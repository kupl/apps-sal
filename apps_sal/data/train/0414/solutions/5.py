from heapq import heapify , heappop , heappush
class Solution:
    def getWinner(self, lis: List[int], k: int) -> int:
        n = len(lis)
        heap=[]
        heapify(heap)
        has=[0]*(max(lis)+10)
        heappush(heap,-lis[0])
        for i in range(1,n):
            heappush(heap,-lis[i])
            #print(heap)
            a = - heappop(heap)
            has[a]+=1
            if has[a]>=k:
                return a
            heappush(heap,-a)
         #   print(heap)
        return max(lis)
    


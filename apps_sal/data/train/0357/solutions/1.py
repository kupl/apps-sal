class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        
#         runzero, maxzero = 0,0
        
#         for i, seat in enumerate(seats):
            
#             if seat==0:
#                 runzero += 1
#                 maxzero = max(maxzero, runzero)
#             else:
#                 runzero=0
                
#         ans = (maxzero+1)//2
#         startmax = seats.index(1)
#         endmax = seats[::-1].index(1)
#         return max(ans, startmax, endmax)

        anspointer = -float('inf')
        prvpointer = None
        
        for i, seat in enumerate(seats):
            
            if seat==1:
                if prvpointer == None:
                    anspointer = i
                    # prvpointer = i
                else:
                    anspointer = max(anspointer, (i-prvpointer)//2)
                
                prvpointer = i
        
        anspointer = max(anspointer, len(seats)-1-prvpointer)
        
        return anspointer

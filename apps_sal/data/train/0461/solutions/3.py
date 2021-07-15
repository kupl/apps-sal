


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        
        reports = {}
        for i,e in enumerate(manager):
            if e not in reports:
                reports[e] = []
            reports[e].append(i)
                
        accum = [0]*n
        todo = [-1]
        while todo:
            curr = todo.pop()
            mxxR = 0
            if curr not in reports:
                continue
            for r in reports[curr]:
                todo.append(r)
                accum[r] += informTime[r] + accum[manager[r]]
        return max(accum)
                
            
                
        
#         talktime = {}
#         mxx = -1
#         for i,m in enumerate(manager):
#             mxx = max(mxx, self.calc(i, manager, informTime))
#         return mxx
                
#     def calc(self,e, manager, informTime):
#         if e == -1:
#             return 0
#         return informTime[e] + self.calc(manager[e], manager, informTime)
        
        


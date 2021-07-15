class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = {}
        for i,man in enumerate(manager):
            if man == -1:
                continue
            if man not in subs:
                subs[man] = set()
            subs[man].add(i)
            
        queue = [(headID, 0)]
        maxInformTime = 0
        
        while queue:
            curr,informedAt = queue.pop()
            if curr not in subs:
                continue
                
            emps = subs[curr]  
            for e in emps:
                currInformTime = informTime[curr] + informedAt
                maxInformTime = max(maxInformTime, currInformTime)
                queue.append((e,currInformTime))
                
        return maxInformTime


from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        res = 0
        nextdict = defaultdict(set)
        timedict = defaultdict(int)
        for i1, m in enumerate(manager):
            nextdict[m].add(i1)
        for i1, t in enumerate(informTime):
            timedict[i1] = t
        
        visit = set()
        q = [(headID, 0)]
        while q:
            this = q[-1]
            visit.add(this[0])
            flag = False
            for nexte in nextdict[this[0]]:
                if nexte not in visit:
                    q.append((nexte, this[1]+timedict[this[0]]))
                    res = max(res, this[1]+timedict[this[0]])
                    flag = True
                    break
            if not flag:
                q.pop()
        return res
        


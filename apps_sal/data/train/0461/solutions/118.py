class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return 0
        t = 0
        m = {}
        start = None
        for i in range(len(manager)):
            if manager[i] != -1:
                if manager[i] in m:
                    m[ manager[i] ].append( i )
                else:
                    m[ manager[i] ] = [ i ]
            else:
                start = i
        q = []
        q.append((start,informTime[start]))
        hi = 0 # max value
        while (len(q) > 0):
            # print(q)
            out = q.pop(0)
            index = out[0]
            cost = out[1]
            if cost > hi: hi = cost
            if index in m:
                for i in m[index]:
                    q.append((i, cost + informTime[i]))
        
        return hi

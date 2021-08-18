class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        if len(manager) == 1:
            return informTime[0]

        d = defaultdict(list)
        for i, e in enumerate(manager):
            d[e].append(i)

        '''
        q=[d[-1]]
        mt=1
        time=-1
        while q:
            time+=mt
            mt=0
            print(\"TIme:- \",time,\"  \",\"Queue:- \",q)
            n=len(q)
            for i in range(n):
                x=q.pop(0)
                if type(x) != int:
                    mt = max(mt,informTime[x[0]])
                    for e in d[x[0]]:
                        q.append(e)
                else:
                    mt = max(mt,informTime[x])
                    for e in d[x]:
                        q.append(e)
        return time
        '''

        self.time = 0

        def dfs(x, mt):

            if type(x) != int:
                if not d[x[0]]:
                    self.time = max(mt, self.time)
                for e in d[x[0]]:
                    dfs(e, mt + informTime[x[0]])
            else:
                if not d[x]:
                    self.time = max(mt, self.time)
                for e in d[x]:
                    dfs(e, mt + informTime[x])

        dfs(d[-1], 0)
        return self.time

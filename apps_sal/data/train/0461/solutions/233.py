class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if len(manager) == 1:
            return informTime[0]
        d = defaultdict(list)
        for (i, e) in enumerate(manager):
            d[e].append(i)
        '\n        q=[d[-1]]\n        mt=1\n        time=-1\n        while q:\n            time+=mt\n            mt=0\n            print("TIme:- ",time,"  ","Queue:- ",q)\n            n=len(q)\n            for i in range(n):\n                x=q.pop(0)\n                if type(x) != int:\n                    mt = max(mt,informTime[x[0]])\n                    for e in d[x[0]]:\n                        q.append(e)\n                else:\n                    mt = max(mt,informTime[x])\n                    for e in d[x]:\n                        q.append(e)\n        return time\n        '
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

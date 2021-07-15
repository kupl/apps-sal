class DSU:
    def __init__(self, n):
        self.parent = []
        for i in range(n + 2):
            self.parent.append(i)
        self.size = []
        for i in range(n + 2):
            self.size.append(1)
    def union(self, u, v):
        pu = self.find(u)
        pv  = self.find(v)
        if pu == pv:
            return
        if self.size[pv] > self.size[pu]:
            pu, pv = pv, pu
        #pu is bigger
        self.parent[pv] = pu
        self.size[pu] += self.size[pv]
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        current_arr = [-1] * (len(arr) + 2)
        dsu = DSU(len(arr)+2)
        res = -1
        cur_sol = set()
        for i, val in enumerate(arr):
            if current_arr[val] == 1:
                continue
            else:
                current_arr[val] = 1
                if current_arr[val - 1] == 1:
                    dsu.union(val, val - 1)
                if current_arr[val + 1] == 1:
                    dsu.union(val, val + 1)
                pv = dsu.find(val)
                if dsu.size[pv] == m:
                    res = i + 1
                    cur_sol.add(pv)
                found = False
                for cs in cur_sol:
                    pcs = dsu.find(cs)
                    if dsu.size[pcs] == m:
                        found = True
                if found == True:
                    res = i + 1
                #res = i + 1
        return res


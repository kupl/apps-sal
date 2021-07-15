class Union_find:
    def __init__(self, MAX: int,target):
        self.fa = [i for i in range(MAX)]
        self.cnt = [1 for _ in range(MAX)]
        self.exist = 0
        self.target = target
        self.root_map = collections.defaultdict(set)

    def find(self, u: int) -> int:
        if self.fa[u] == u:
            return u

        self.fa[u] = self.find(self.fa[u])
        return self.fa[u]

    def union(self, u: int, v: int):
        u, v = self.find(u), self.find(v)
        if u == v:
            return None

        if self.cnt[u] < self.cnt[v]:
            u, v = v, u
        vn = int(self.cnt[v])
        un = int(self.cnt[u])
        try:
            self.root_map[vn].remove(v)
        except:
            pass
        self.cnt[u] = vn + un
        try:
            self.root_map[un].remove(u)
        except:
            pass
        self.root_map[vn+un].add(u)
        self.fa[v] = u
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        ct = 0
        l = [0 for i in arr]
        n = 0
        res = -1
        uf = Union_find(len(arr),m)
        for i in arr:
            l[i-1] = 1
            ct += 1
            flag = False
            if i-2>-1 and l[i-2] == 1:
                uf.union(i-1,i-2)
                flag = True
            if i<len(arr) and l[i] == 1:
                uf.union(i-1,i)
                flag = True
            if not flag:
                uf.root_map[1].add(i-1)
            if len(uf.root_map[m])>0:
                res = ct
        return res

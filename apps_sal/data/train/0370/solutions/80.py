class node:
    def __init__(self, val):
        self.val = val
        self.next = []


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # l=[node(i) for i in A]
        # for i in range(len(l)):
        #     for j in range(len(l)):
        #         if math.gcd(l[i].val,l[j].val)>1 and i!=j:
        #             l[j].next.append(i)
        # # for i in range(len(l)):
        # #     print(l[i].next)
        # # print(l)
        # # def bfs(n,m):
        # #     nonlocal l,vis
        # #     # print(n,m,vis)
        # #     vis[n]=True
        # #     m+=1
        # #     # k=m
        # #     for i in l[n].next:
        # #         if not vis[i]:
        # #             m=dfs(i,m)
        # #     return m
        # def bfs(n):
        #     nonlocal l,vis
        #     q=[n]
        #     # vis[n]=True
        #     m=0
        #     while q:
        #         # print(q,vis)
        #         k=[]
        #         for i in q:
        #             if not vis[i]:
        #                 vis[i]=True
        #                 k.extend(l[i].next)
        #                 m+=1
        #         q=k
        #     return m
        # mi=0
        # vis=[False for i in range(len(l))]
        # for i in range(len(l)):
        #     if not vis[i]:
        #         mi=max(mi,bfs(i))
        # return mi
        p = [2]
        for i in range(3, int(max(A)**0.5) + 1, 2):
            for y in p:
                if i % y == 0:
                    break
            else:
                p.append(i)
        f = collections.defaultdict(list)
        for a in A:
            x = a
            for pp in p:
                if pp**2 > x:
                    break
                if x % pp == 0:
                    f[a].append(pp)
                    while x % pp == 0:
                        x = x // pp
            if x > 1:
                f[a].append(x)
                p.append(x)
        # print(p,f)
        p = list(set(p))
        n = len(p)
        p2i = {pp: i for i, pp in enumerate(p)}
        par = [i for i in range(n)]

        def find(i):
            if i != par[i]:
                par[i] = find(par[i])
            return par[i]

        def union(i, j):
            pi, pj = find(i), find(j)
            if pi != pj:
                par[pi] = pj
        for a in A:
            if f[a]:
                p0 = f[a][0]
                for pp in f[a][1:]:
                    union(p2i[p0], p2i[pp])
        # l=[find(p2i[f[a][0]]) for a in A]
        c = collections.Counter(find(p2i[f[a][0]]) for a in A if f[a])
        return max(c.values())

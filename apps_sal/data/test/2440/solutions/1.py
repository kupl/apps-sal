from collections import deque
import sys
input = sys.stdin.readline


class LowestCommonAncestor():
    def __init__(self, tree, root):
        self.n = len(tree)
        self.depth = [0] * self.n
        self.log_size = (self.n).bit_length()
        self.parent = [[-1] * self.n for i in range(self.log_size)]

        q = deque([(root, -1, 0)]) 
        while q:
            v, par, dist = q.pop()
            self.parent[0][v] = par
            self.depth[v] = dist
            for child_v in tree[v]:
                if child_v != par:
                    self.depth[child_v] = dist + 1
                    q.append((child_v, v, dist + 1))

        for k in range(1, self.log_size):
            for v in range(self.n):
                self.parent[k][v] = self.parent[k-1][self.parent[k-1][v]]
            
    def lca(self, u, v):
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        for k in range(self.log_size):
            if (self.depth[v] - self.depth[u] >> k) & 1:
                v = self.parent[k][v]
        if u == v:
            return u
          
        for k in reversed(range(self.log_size)):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]


n = int(input())
info = [list(map(int, input().split())) for  i in range(n - 1)]

tree = [[] for i in range(n)]
for i in range(n - 1):
    a, b = info[i]
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)
    
lca = LowestCommonAncestor(tree, 0)

q = int(input())
query = [list(map(int, input().split())) for i in range(q)]
    
for i in range(q):
    x, y, a, b, k = query[i]
    lca_ab = lca.lca(a - 1, b - 1)
    ab = lca.depth[a - 1] + lca.depth[b - 1] - 2 * lca.depth[lca_ab]
    lca_xy = lca.lca(x - 1, y - 1)
    xy = lca.depth[x - 1] + lca.depth[y - 1] - 2 * lca.depth[lca_xy]

    lca_ax = lca.lca(a - 1, x - 1)
    lca_ay = lca.lca(a - 1, y - 1)
    lca_bx = lca.lca(b - 1, x - 1)
    lca_by = lca.lca(b - 1, y - 1)
    
    ax = lca.depth[a - 1] + lca.depth[x - 1] - 2 * lca.depth[lca_ax]
    ay = lca.depth[a - 1] + lca.depth[y - 1] - 2 * lca.depth[lca_ay]
    bx = lca.depth[b - 1] + lca.depth[x - 1] - 2 * lca.depth[lca_bx]
    by = lca.depth[b - 1] + lca.depth[y - 1] - 2 * lca.depth[lca_by]
    if ab <= k and k % 2 == ab % 2:
        print("YES")
    elif ax+1+by <= k and k % 2 == (ax+1+by) % 2:
        print("YES")
    elif ay+1+bx <= k and k % 2 == (ay+1+bx) % 2:
        print("YES")
    else:
        print("NO")

from collections import defaultdict


class UnionFind:

    def __init__(self, num):
        self.roots = [i for i in range(num + 1)]
        self.ranks = [1 for _ in range(num + 1)]

    def get_root(self, node):
        if node != self.roots[node]:
            self.roots[node] = self.get_root(self.roots[node])
        return self.roots[node]

    def unite(self, node_1, node_2):
        root_1 = self.get_root(node_1)
        root_2 = self.get_root(node_2)
        if root_1 == root_2:
            return
        elif self.ranks[root_1] > self.ranks[root_2]:
            self.roots[root_2] = root_1
        else:
            if self.ranks[root_1] == self.ranks[root_2]:
                self.ranks[root_2] += 1
            self.roots[root_1] = root_2

    def get_root_list(self):
        for i in range(len(self.roots)):
            self.get_root(i)
        return self.roots


(n, m) = map(int, input().split())
bef = list(map(int, input().split()))
aft = list(map(int, input().split()))
dif = [0] * n
for k in range(n):
    dif[k] = aft[k] - bef[k]
u = UnionFind(n)
for _ in range(m):
    (x, y) = map(int, input().split())
    u.unite(x, y)
u_list = u.get_root_list()
u_dict = defaultdict(set)
for z in range(n + 1):
    r = u_list[z]
    u_dict[r].add(z)
u_dict.pop(0)
flag = True
for d in u_dict.values():
    cnt = 0
    for dd in d:
        cnt += dif[dd - 1]
    if cnt != 0:
        flag = False
        break
if flag:
    print('Yes')
else:
    print('No')

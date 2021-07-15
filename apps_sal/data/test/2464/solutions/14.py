class UnionFindVerSize():
    def __init__(self, N):
        self._parent = [n for n in range(0, N)]
        self._size = [1] * N

    def find_root(self, x):
        if self._parent[x] == x: return x
        self._parent[x] = self.find_root(self._parent[x])
        return self._parent[x]

    def unite(self, x, y):
        gx = self.find_root(x)
        gy = self.find_root(y)
        if gx == gy: return

        if self._size[gx] < self._size[gy]:
            self._parent[gx] = gy
            self._size[gy] += self._size[gx]
        else:
            self._parent[gy] = gx
            self._size[gx] += self._size[gy]

    def get_size(self, x):
        return self._size[self.find_root(x)]

    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def calc_group_num(self):
        N = len(self._parent)
        ans = 0
        for i in range(N):
            if self.find_root(i) == i:
                ans += 1
        return ans

import sys

input=sys.stdin.readline
n=int(input())
uf0=UnionFindVerSize(n)
uf1=UnionFindVerSize(n)
for i in range(n-1):
    x,y,c=map(int,input().split())
    if c==0:
        uf0.unite(x-1,y-1)
    else:
        uf1.unite(x-1,y-1)

data=[0]*n
cnt=[0]*n
for i in range(n):
    root=uf1.find_root(i)
    data[root]+=uf0.get_size(i)
    cnt[root]+=1

ans=sum(data[i]*cnt[i] for i in range(n))
print(ans-n)

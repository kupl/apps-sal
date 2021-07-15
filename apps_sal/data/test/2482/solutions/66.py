"""
道路でつながっているやつが鉄道でもつながっているかどうかを調べるにはどうすればいい？
普通に木ごとのサイズを求めておけばいいのか？

道路ネットワークを根ごとにグルーピングする。その中で、さらに鉄道の根ごとにグルーピングする。
でchooseでペア数を求めれば良い。

"""
import math
import sys
sys.setrecursionlimit(200000)
class UnionFind():
    def __init__(self,n):
        self.parents = [i for i in range(n+1)]

    def find(self,x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self,x,y):
        self.parents[self.find(y)]=self.find(x)

N,K,L = list(map(int,input().split()))
A = UnionFind(N)
B = UnionFind(N)
for i in range(K):
    p,q = list(map(int,input().split()))
    A.union(p,q)

for i in range(L):
    r,s = list(map(int,input().split()))
    B.union(r,s)


group = {}
for i in range(1,N+1):
    roadRoot = A.find(i)
    if roadRoot not in group:
        group[roadRoot] = {}
    railRoot = B.find(i)
    if railRoot not in group[roadRoot]:
        group[roadRoot][railRoot] = []
    group[roadRoot][railRoot].append(i)

ans = [[]for _ in range(N)]
for i in list(group.items()):
    for j in list(i[1].values()):
        for k in j:
            ans[k-1] = str(len(j))

ans = " ".join(ans)
print(ans)


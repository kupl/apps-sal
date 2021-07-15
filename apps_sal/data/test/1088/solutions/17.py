def MI():
    return map(int, input().split())

n,k= MI()
mod=998244353
framod=[1]
def framod_calc(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
        framod.append(a)
framod_calc(n+1, mod)
def permmod(n, k, mod):
    if n<k: return 0
    a=framod[n]
    c=framod[n-k]
    return (a * pow(c, mod-2, mod)) % mod

mat=[]
matinv=[[0]*n for _ in range(n)]
for i in range(n):
    mat.append(list(MI()))

for i in range(n):
    for j in range(n):
        matinv[i][j]=mat[j][i]

esrow=[]
escol=[]

for i in range(n):
    for j in range(i+1, n):
        flg=True
        for p in range(n):
            if mat[i][p]+mat[j][p]>k:
                flg=False
                break
        if flg:
            esrow.append((i,j))

for i in range(n):
    for j in range(i+1, n):
        flg=True
        for p in range(n):
            if matinv[i][p]+matinv[j][p]>k:
                flg=False
                break
        if flg:
            escol.append((i,j))

class UnionFind(object): # sizeをO(1)で引けるversion
    def __init__(self, n=1):
        self.n=n
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.sizebox = [1]*n
    def find(self, x): # xの属する連結成分の代表元
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def union(self, x, y): # x,yを連結、ついでにサイズも連結
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.sizebox[x]+=self.sizebox[y]
    def same(self, x, y): # x,yが連結かどうか
        return self.find(x) == self.find(y)
    def size(self,x): # xの属する連結sizeをO(1)で出す
        x = self.find(x)
        return self.sizebox[x]
    def allfind(self): # findを1周する
        for i in range(self.n):
            self.find(i)

ufr=UnionFind(n)
ufc=UnionFind(n)

for i,j in esrow:
    ufr.union(i,j)

for i,j in escol:
    ufc.union(i,j)

for i in range(n):
    ufr.find(i)
    ufc.find(j)

from collections import Counter
cpar=Counter(ufc.par)
rpar=Counter(ufr.par)

ans=1

for k in cpar.keys():
    x=cpar[k]
    ans*=permmod(x,x,mod)
    ans%=mod

for k in rpar.keys():
    x=rpar[k]
    ans*=permmod(x,x,mod)
    ans%=mod

print(ans%mod)

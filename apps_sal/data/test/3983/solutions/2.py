class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)) #親ノード
        self.size = [1]*n #グループの要素数
 
    def root(self, x): #root(x): xの根ノードを返す．
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x 
 
    def merge(self, x, y): #merge(x,y): xのいる組とyのいる組をまとめる
        x, y = self.root(x), self.root(y)
        if x == y: return False
        if self.size[x] < self.size[y]: x,y=y,x #xの要素数が大きいように
        self.size[x] += self.size[y] #xの要素数を更新
        self.parent[y] = x #yをxにつなぐ
        return True
 
    def issame(self, x, y): #same(x,y): xとyが同じ組ならTrue
        return self.root(x) == self.root(y)
        
    def getsize(self,x): #size(x): xのいるグループの要素数を返す
        return self.size[self.root(x)]


# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read



def solve():
    # 0: 先手、1: 後手
    n,m = list(map(int, readline().split()))

    UF = UnionFind(n)
    for _ in range(m):
        a,b = list(map(int, readline().split()))
        UF.merge(a-1,b-1)
    
    s1 = UF.getsize(0)%2
    s2 = UF.getsize(n-1)%2
    
    #print(n%4,m%2,s1,s2)
    
    if n%4==0:
        if s1==s2==m%2:
            return 1
        return 0
    elif n%4==2:
        if s1==s2==1-m%2:
            return 1
        return 0
    elif n%4==1:
        if m%2==0: return 1
        else: return 0
    elif n%4==3:
        if m%2==0: return 0
        else: return 1



ans = ["First","Second"]
T, = list(map(int, readline().split()))
for i in range(T):
    x = solve()
    print((ans[x]))





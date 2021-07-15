n,m=map(int,input().split())
class WarshallFloyd:
#O(V^3)で任意２頂点の最短距離
    def __init__(self,n,_first_index=0):
        self.v = n
        self._first_idx=_first_index
        self.d = [[1e100]*(n+_first_index) for _ in range(n+_first_index)]
        for i in range(n+_first_index):
            self.d[i][i] = 0

    def path(self,x,y,c):
        if x == y:
            return False
        self.d[x][y] = c
        self.d[y][x] = c
        return True

    def build(self):
        f=self._first_idx
        for k in range(f,self.v+f):
            for i in range(f,self.v+f):
                for j in range(f,self.v+f):
                    self.d[i][j] = min(self.d[i][j], self.d[i][k] + self.d[k][j])
        return self.d
w=WarshallFloyd(n,1)
l=[]
for i in range(m):
    x,y,c=map(int,input().split())
    w.path(x,y,c)
    x,y=sorted([x,y])
    l.append([x,y,c])
d=w.build()
ans=0
for a,s,c in l:
    f=1
    for y in range(1,n+1):
        if d[y][s]==d[y][a]+c:f=0;break
    ans+=f
print(ans)

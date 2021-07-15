class Union:
    def __init__(self, n, list_k):
        self.p    = {i:i for i in range(n+1)}
        self.rank = {i:0 for i in range(n+1)} 
        
        for k in list_k:
            self.rank[k] = 1
            
    def find(self, x):
        if x < 0: return x
    
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        if x < 0 or y < 0:return
        
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.p[x]     = y
                self.rank[y] += self.rank[x]
            else:
                self.p[y]     = x
                self.rank[x] += self.rank[y]
                
n, m, k  = list(map(int, input().split()))
list_k   = list(map(int, input().split()))
edge  = []

for _ in range(m):
    u, v, w = list(map(int, input().split()))
    edge.append((u,v,w))
    
edge = sorted(edge, key=lambda x:x[2])

U   = Union(n, list_k)
val = 0

for u, v, w in edge:
    if u == v: continue
        
    par_1 =  U.find(u)
    par_2 =  U.find(v)    
        
    if par_1 == par_2:
        continue
        
    if U.rank[par_1] + U.rank[par_2] == k:
        val = w
        break
    
    U.union(u, v)

s = ''
for _ in  range(len(list_k)):
    s += str(val) + ' '    
                
print(s)
                
#2 3 2
#2 1
#1 2 3
#1 2 2
#2 2 1


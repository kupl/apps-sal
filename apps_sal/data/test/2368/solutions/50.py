n, m = map(int, input().rstrip().split(" "))

A = list(map(int, input().rstrip().split(" ")))
B = list(map(int, input().rstrip().split(" ")))

M = []
for i in range(m):
    a, b = map(int, input().rstrip().split(" "))
    M.append((a-1, b-1))

class UnionFind:
    
    Par = []
    Total = []
    
    
    def __init__(self, n_):
        for i in range(n_):
            self.Par.append(i)
            self.Total.append(0)
    
    def root(self, x):
        if(self.Par[x] == x):
            ret = x
        else:
            ret = self.root(self.Par[x])
        return ret
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if(x > y):
            self.Par[x] = y
        elif(x < y):
            self.Par[y] = x
    def same(x, y):
        x = self.root(x)
        y = self.root(y)
        if(x==y):
            ret = True
        else:
            ret = False
        return ret
    def printf(self):
        print(self.Par)
        print(self.Total)
        
        
union = UnionFind(n)
for i in M:
    c, d = i
    union.unite(c, d)

Dif = []
for i in range(n):
    dif = B[i] - A[i]
    Dif.append(dif)

Zero = [0 for i in range(n)]
for i in range(n):
    root = union.root(i)
    Zero[root] += Dif[i]

isOK = True
for zero in Zero:
    if(zero != 0):
        isOK = False


if(isOK == True):
    print("Yes")
else:
    print("No")

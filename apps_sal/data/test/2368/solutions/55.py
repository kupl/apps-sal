def root(x):
    if r[x] < 0:
        return x
    else:
        r[x] = root(r[x])
        return r[x]
 
def unite(x, y):
    x = root(x)
    y = root(y)
    if x != y:
        if r[x] > r[y]:
            x,y = y,x
        r[x] += r[y]
        r[y] = x

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
r = [-1] * n
for i in range(m):
    c,d = map(int,input().split())
    c -= 1
    d -= 1
    unite(c,d)
p = [0] * n
q = [0] * n
for i in range(n):
    if r[i] < 0:
        x = i
    else:
        x = root(i)
    p[x] += a[i]
    q[x] += b[i]
for i in range(n):
    if p[i] != q[i]:
        print('No')
        return
print('Yes')    

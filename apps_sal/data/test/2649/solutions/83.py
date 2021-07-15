n = int(input())
z = []
w = []
for i in range(n):
    x,y = map(int,input().split())
    z.append(x+y)
    w.append(x-y)
zmax = max(z)-min(z)
wmax = max(w)-min(w)
print(max(zmax,wmax))

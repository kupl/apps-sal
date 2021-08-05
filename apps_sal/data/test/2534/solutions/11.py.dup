r, c = map(int, input().split())
mat = []
rmin = []
cmax = []
d = {}
f = 0
for i in range(r):
    l = list(map(int, input().split()))
    mat.append(l)
for i in range(r):
    x = min(mat[i])
    rmin.append(x)
for i in range(c):
    x = []
    for j in range(r):
        x.append(mat[j][i])
    cmax.append(max(x))
for i in rmin:
    if(i in cmax):
        print(i)
        f = 1
        break
if(f == 0):
    print("GUESS")

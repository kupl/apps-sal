import itertools as it
n,c= map(int,input().split())
dtab = []
dtab.append([0 for _ in range(c+1)])
for i in range(c):dtab.append([0] + list(map(int,input().split())))
ctab = []
ctab.append([0 for _ in range(n+1)])
for i in range(n):ctab.append([0]+list(map(int,input().split())))
ssd = [{},{},{}]
for i in range(1,n+1):
    for j in range(1,n+1):
        temp = (i+j)%3
        temp2 = ctab[i][j]
        ssd[temp][temp2] = ssd[temp].get(temp2,0) + 1
e = [i+1 for i in range(c)]
cpm = it.permutations(e, 3)
ming=999999999
for f in cpm:
    fl=list(f)
    cg = 0
    for i in range(3):
        for p in ssd[i].keys():cg += dtab[p][fl[i]] * ssd[i][p]
    ming = min(ming,cg)
print(ming)

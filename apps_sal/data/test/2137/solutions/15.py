import bisect
(n, a, b) = map(int, input().split(' '))
x = [0] * n
vx = [0] * n
vy = [0] * n
for i in range(n):
    (x[i], vx[i], vy[i]) = map(int, input().split(' '))
ntypes = dict()
for i in range(n):
    ntype = -a * vx[i] + 1 * vy[i]
    currSet = ntypes.get(ntype, set())
    currSet.add(i)
    ntypes[ntype] = currSet
result = 0
for key in ntypes.keys():
    currSet = ntypes[key]
    currLen = len(currSet)
    vtypes = dict()
    for i in currSet:
        vtype = vx[i] * 1 + vy[i] * a
        vtypes[vtype] = vtypes.get(vtype, 0) + 1
    for key in vtypes.keys():
        curr = vtypes[key]
        result += curr * (currLen - curr)
print(result)

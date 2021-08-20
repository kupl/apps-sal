from collections import defaultdict


def rp():
    s = input().split()
    return (s[0], int(s[1]))


ps = {}
n = int(input())
for i in range(n):
    p = rp()
    d = []
    for _ in range(int(input())):
        d += [rp()]
    ps[p] = d
    if i != n - 1:
        input()
root = list(ps.keys())[0]
q = [(root, 0)]
u = {root[0]: (root[1], 0)}
for (i, l) in q:
    isp = i
    if isp[0] in u and isp[1] != u[isp[0]][0]:
        continue
    for p in ps[i]:
        psp = p
        if psp[0] not in u or (u[psp[0]][1] == l + 1 and u[psp[0]][0] < psp[1]):
            u[psp[0]] = (psp[1], l + 1)
            q.append((psp, l + 1))
del u[root[0]]
print(len(u))
for i in sorted(u):
    print(i, u[i][0])

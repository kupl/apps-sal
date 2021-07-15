n = int(input())
tr = {}
p = [int(s) for s in input().split()]
for i in range(n-1):
    if not tr.get(p[i]-1):
        tr[p[i]-1] = []
    tr[p[i]-1].append(i+1)
# print(tr)
lc = [-1 for i in range(n)]
def get_lc(i):
    if lc[i] == -1:
        if tr.get(i):
            lc[i] = 0
            for j in tr[i]:
                lc[i] += get_lc(j)
        else:
            lc[i] = 1
    return lc[i]
for i in range(n-1, -1, -1):
    get_lc(i)
print(*sorted(lc))

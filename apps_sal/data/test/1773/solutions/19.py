def R():
    return list(map(int, input().split()))


n = R()[0]
a = []
for i in range(n):
    a.append(R())
a.sort()
npos = 0
nneg = 0
for i in a:
    if i[0] > 0:
        npos += 1
    else:
        nneg += 1
ans = 0
if npos >= nneg + 1:
    ans = sum((i[1] for i in a[:nneg + nneg + 1]))
else:
    ans = sum((i[1] for i in a[max(0, nneg - 1 - npos):]))
print(ans)

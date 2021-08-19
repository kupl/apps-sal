n = int(input())
b = []
mx = []
mn = []
mx_i = []
mn_i = []
for i in range(n):
    (u, v) = [int(x) for x in input().strip().split()]
    if u > v:
        mx.append((u, v))
        mx_i.append(i + 1)
    else:
        mn.append((u, v))
        mn_i.append(i + 1)
if len(mx) > len(mn):
    print(len(mx))
    res = [x[1] for x in sorted(zip(mx, mx_i))]
else:
    print(len(mn))
    res = [x[1] for x in sorted(zip(mn, mn_i), reverse=True)]
for r in res:
    print(r, end=' ')
print()

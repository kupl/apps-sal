n, m = map(int, input().split())
isen = []
for i in range(m):
    isen.append(0)
for i in range(n):
    a = input().split()
    k = int(a[0])
    for j in range(k):
        cur = int(a[j + 1])
        isen[cur - 1] = 1
ok = True
for i in isen:
    if i == 0:
        ok = False
if ok:
    print("YES")
else:
    print("NO")

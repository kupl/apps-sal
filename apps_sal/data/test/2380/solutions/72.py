(n, m) = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
bc = []
for i in range(m):
    bc.append(list(map(int, input().split())))
bc.sort(key=lambda x: x[1], reverse=True)
lis = []
for i in range(m):
    if len(lis) >= n:
        break
    for _ in range(bc[i][0]):
        lis.append(bc[i][1])
while len(lis) < n:
    lis.append(0)
s = 0
for i in range(n):
    s += max(a[i], lis[i])
print(s)

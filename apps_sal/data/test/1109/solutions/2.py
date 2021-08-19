(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = []
c = []
for i in range(k):
    c.append([0, 0])
for i in range(k):
    b.append(a[i])
par = True
ans = 0
for i in range(n):
    if a[i] != b[i % k]:
        par = False
    c[i % k][a[i] - 1] += 1
if par:
    print(0)
else:
    for i in range(k):
        ans += min(c[i])
    print(ans)

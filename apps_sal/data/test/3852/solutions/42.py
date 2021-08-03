n = int(input())
a = list(map(int, input().split()))
ma = max(a)
mai = a.index(ma)
mi = min(a)
mii = a.index(mi)
ans = []
if abs(ma) >= abs(mi):
    for i in range(n):
        a[i] += ma
        ans.append((mai + 1, i + 1))
    for i in range(1, n):
        a[i] += a[i - 1]
        ans.append((i, i + 1))
else:
    for i in range(n):
        a[i] += mi
        ans.append((mii + 1, i + 1))
    for i in range(n - 2, -1, -1):
        a[i] += a[i + 1]
        ans.append((i + 2, i + 1))
print(len(ans))
for i in ans:
    print(*i)

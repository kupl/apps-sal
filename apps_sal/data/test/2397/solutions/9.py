li = input().split()
n = int(li[0])
k = int(li[1])
a = input().split()
for i in range(n):
    a[i] = int(a[i])
for i in range(n - 2, -1, -1):
    a[i] += a[i + 1]
sa = sorted(a[1:])
ans = a[0]
for i in range(k - 1):
    ans += sa[n - 2 - i]
print(ans)

(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = 100
for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            ans = min(ans, a[i])
ans = min(ans, min(a[0] * 10 + b[0], b[0] * 10 + a[0]))
print(ans)

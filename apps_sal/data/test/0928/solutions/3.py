n, k = map(int, input().split())
a = list(map(int, input().split()))
s = 0
j = 0
ans = 0
for i in range(n):
    s += a[i]
    while s >= k:
        ans += (n - i)
        s -= a[j]
        j += 1
print(ans)

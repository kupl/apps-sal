n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n):
    while (k * 2 < a[i]):
        k *= 2
        ans += 1
    k = max(k, a[i])
print(ans)

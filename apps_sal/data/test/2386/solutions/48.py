n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    a[i] = a[i] - (i + 1)
    ans += abs(a[i])
a.sort()
for b in a[n // 2 - 1:n // 2 + 1]:
    tmp = 0
    for i in range(n):
        tmp += abs(a[i] - b)
    ans = min(ans, tmp)
print(ans)

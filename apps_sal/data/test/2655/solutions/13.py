n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
ans = 0
if n % 2 == 0:
    for i in range(n // 2):
        if i == 0:
            ans += a[i]
            continue
        ans += a[i] * 2
else:
    for i in range(n // 2 + 1):
        if i == 0:
            ans += a[i]
            continue
        ans += a[i] * 2
if n % 2 == 1:
    ans -= a[i]
print(ans)

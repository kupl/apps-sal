n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    if a[i] >= b[i]:
        ans += b[i]
    else:
        c = b[i] - a[i]
        if a[i + 1] >= c:
            a[i + 1] -= c
            ans += a[i] + c
        else:
            ans += a[i] + a[i + 1]
            a[i + 1] = 0

print(ans)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    if a[i] >= b[i]:
        ans += b[i]
    else:
        ans += a[i]
        if a[i + 1] > b[i] - a[i]:
            ans += b[i] - a[i]
            a[i + 1] -= b[i] - a[i]
        else:
            ans += a[i + 1]
            a[i + 1] = 0
print(ans)

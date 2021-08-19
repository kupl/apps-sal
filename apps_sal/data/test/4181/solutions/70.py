n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    if b[i] <= a[i]:
        ans += b[i]
    else:
        ans += a[i]
        b[i] -= a[i]
        if b[i] >= a[i + 1]:
            ans += a[i + 1]
            a[i + 1] = 0
        else:
            ans += b[i]
            a[i + 1] -= b[i]
print(ans)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    if a[i] <= b[i]:
        ans += a[i]
        if b[i] - a[i] <= a[i + 1]:
            ans += b[i] - a[i]
            a[i + 1] -= b[i] - a[i]
        else:
            ans += a[i + 1]
            a[i + 1] = 0
    elif a[i] - b[i] > 0:
        ans += b[i]
print(ans)

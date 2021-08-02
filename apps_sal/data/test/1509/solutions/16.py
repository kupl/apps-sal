n = int(input())
a = [int(x) for x in input().split()]

ans = a[0] * (n - a[0] + 1)
for i in range(1, n):
    if a[i] > a[i - 1]:
        ans += (a[i] - a[i - 1]) * (n - a[i] + 1)
    elif a[i] < a[i - 1]:
        ans += a[i] * (a[i - 1] - a[i])
print(ans)

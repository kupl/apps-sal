n = int(input())
a = [int(i) for i in input().split()]
for i in range(n - 1):
    a[i + 1] += a[i]
j = 0
k = 2
ans = 10 ** 9
for i in range(1, n - 1):
    while abs(a[j] * 2 - a[i]) > abs(a[j + 1] * 2 - a[i]):
        j += 1
    while abs(a[k] * 2 - a[i] - a[n - 1]) > abs(a[k + 1] * 2 - a[i] - a[n - 1]):
        k += 1
    t = [a[j], a[i] - a[j], a[k] - a[i], a[n - 1] - a[k]]
    ans = min(ans, max(t) - min(t))
print(ans)

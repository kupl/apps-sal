n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort(key=lambda x: (x % 10), reverse=True)
i = 0
while (i < n and k > 0 and a[i] % 10 > 0):
    t = max(0, k - 10 + a[i] % 10)
    a[i] = a[i] // 10 * 10 + min(10, a[i] % 10 + k)
    k = t
    i += 1
i = 0
while (i < n and k > 0):
    t = 100 - a[i]
    a[i] += min(k, t)
    k = max(0, k - t)
    i += 1
ans = 0
for i in a:
    ans += i // 10
print(ans)

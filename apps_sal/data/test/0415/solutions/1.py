n = int(input())
a = [int(x) for x in input().split()]
pref = [0] * n
pref[0] = a[0]
for i in range(1, n):
    pref[i] = a[i] + pref[i - 1]
ans = 0
for t in range(n, 0, -1):
    for i in range(n - t + 1):
        s = pref[i + t - 1]
        if i > 0:
            s -= pref[i - 1]
        if s > 100 * t:
            ans = max(ans, t)
print(ans)

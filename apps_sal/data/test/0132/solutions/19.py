n = int(input())
a = [int(i) for i in input().split()]
ans = 1000000000.0
for j in range(n):
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + a[i - 1]
    for i in range(n):
        ans = min(ans, abs(pref[-1] - 2 * pref[i]))
    a = [a[-1]] + a[:-1]
print(ans)

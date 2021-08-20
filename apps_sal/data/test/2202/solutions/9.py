(n, p) = map(int, input().split())
a = list(map(int, input().split()))
pref = [a[0]]
for i in range(1, n):
    pref.append(pref[-1] + a[i])
tot = pref[-1]
ans = 0
for i in range(n - 1):
    ans = max(ans, pref[i] % p + (pref[-1] - pref[i]) % p)
print(ans)

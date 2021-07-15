mod = int(1e9+7)
s = input()
n = len(s)
pref = [0] * (n+1)
for i in range(n):
    pref[i+1] = (int(s[i]) + pref[i]*10) % mod
for i in range(n):
    pref[i+1] = (pref[i+1] + pref[i]) % mod

res = 0
acc = 0
for i in range(n, 0, -1):
    res += pref[i-1] * pow(10, n-i, mod) + i*acc
    res %= mod
    acc = acc + int(s[i-1]) * pow(10, n-i, mod) % mod
print(res)


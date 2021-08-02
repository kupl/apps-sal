n = int(input())
s = input()
k = 0
ans = 0
if s[n - 1] != s[0]:
    while k < n and s[k] == s[0]:
        k += 1
    ans = k
    k = 0
    while n - 1 - k >= 0 and s[n - 1 - k] == s[n - 1]:
        k += 1
    ans += k
else:
    kl, kr = 0, 0
    while kl < n and s[kl] == s[0]:
        kl += 1
    while n - 1 - kr >= 0 and s[n - 1 - kr] == s[0]:
        kr += 1
    if kl == n:
        ans = n * (n + 1) // 2
    else:
        ans = kl * kr + kl + kr
print((ans + 1) % 998244353)

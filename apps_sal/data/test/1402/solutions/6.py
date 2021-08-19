mod = 1000000007
n = int(input())
s1 = input()
s2 = input()
ans = 1
tc = 1
for i in range(n):
    if s1[i] == '?':
        ans *= 10
        ans %= mod
    if s2[i] == '?':
        ans *= 10
        ans %= mod
for i in range(n):
    if s1[i] != '?' and s2[i] != '?' and (s1[i] > s2[i]):
        break
    if s1[i] == '?' and s2[i] == '?':
        tc *= 55
        tc %= mod
    if s1[i] == '?' and s2[i] != '?':
        tc = tc * (int(s2[i]) + 1)
        tc %= mod
    if s1[i] != '?' and s2[i] == '?':
        tc = tc * (10 - int(s1[i]))
        tc %= mod
    if i == n - 1:
        ans -= tc
        ans = (ans + mod) % mod
tc = 1
for i in range(n):
    if s1[i] != '?' and s2[i] != '?' and (s2[i] > s1[i]):
        break
    if s1[i] == '?' and s2[i] == '?':
        tc *= 55
        tc %= mod
    if s1[i] != '?' and s2[i] == '?':
        tc = tc * (int(s1[i]) + 1)
        tc %= mod
    if s1[i] == '?' and s2[i] != '?':
        tc = tc * (10 - int(s2[i]))
        tc %= mod
    if i == n - 1:
        ans -= tc
        ans = (ans + mod) % mod
tc = 1
for i in range(n):
    if s1[i] != '?' and s2[i] != '?' and (s1[i] != s2[i]):
        break
    if s1[i] == '?' and s2[i] == '?':
        tc *= 10
        tc %= mod
    if i == n - 1:
        ans += tc
        ans = (ans + mod) % mod
print(ans)

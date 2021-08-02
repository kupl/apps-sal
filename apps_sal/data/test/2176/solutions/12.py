import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for y in range(n)]
MOD = 998244353

fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = (fact[i - 1] * i) % MOD

a, b = [0] * n, [0] * n

for x, y in s:
    a[x - 1] += 1
    b[y - 1] += 1

a_count = 1
b_count = 1
for i in range(n):
    a_count *= fact[a[i]]
    a_count %= MOD
    b_count *= fact[b[i]]
    b_count %= MOD

ab_count = 1
count = 1
s.sort()
for i in range(1, n):
    if s[i][1] < s[i - 1][1]:
        ab_count = 0
        break

    if s[i] == s[i - 1]:
        count += 1
    else:
        ab_count *= fact[count]
        ab_count %= MOD
        count = 1

ab_count *= fact[count]
ab_count %= MOD

print((fact[n] - a_count - b_count + ab_count) % MOD)

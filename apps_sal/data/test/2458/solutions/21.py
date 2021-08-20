from sys import stdin, stdout
3
(t, k) = map(int, stdin.readline().split())
a = [0] * 100001
s = [0] * 100001
MOD = 1000000007
for i in range(0, 100001):
    if i < k:
        a[i] = 1
    else:
        a[i] = (a[i - 1] + a[i - k]) % MOD
    s[i] = (s[i - 1] + a[i]) % MOD
for i in range(0, t):
    (l, r) = map(int, stdin.readline().split())
    stdout.write(str((s[r] - s[l - 1] + MOD) % MOD) + '\n')

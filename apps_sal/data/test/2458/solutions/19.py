from sys import stdin, stdout
modconst = 1000000007
(n, k) = list(map(int, stdin.readline().split()))
f = [0] * 100001
ss = [0] * 100001
f[0] = 0
for i in range(1, k):
    f[i] = 1
f[k] = 2
for i in range(k + 1, 100001):
    f[i] = (f[i - 1] + f[i - k]) % modconst
ss[0] = 0
for i in range(1, 100001):
    ss[i] = (ss[i - 1] + f[i]) % modconst
for i in range(n):
    (a, b) = list(map(int, stdin.readline().split()))
    stdout.write(str((ss[b] - ss[a - 1] + modconst) % modconst) + '\n')

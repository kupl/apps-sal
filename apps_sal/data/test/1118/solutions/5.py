def fill():
    nonlocal dp
    dp = [0] * (n + 2)
    for i in range(n + 2):
        dp[i] = [0] * (n + 2)


def compress(v):
    nonlocal n
    nonlocal c
    c = [v[0]]
    for i in range(1, n):
        if v[i] != v[i - 1]:
            c.append(v[i])
    n = len(c)


n = int(input())
v = [int(i) for i in input().split()]
c = []
compress(v)
dp = []
fill()
for i in range(n):
    dp[i][1] = 0
    dp[i][2] = 1

for sz in range(3, n + 1):
    for i in range(n):
        j = i + sz - 1
        if j >= n:
            break
        if c[i] == c[j]:
            dp[i][sz] = dp[i + 1][sz - 2] + 1
        else:
            dp[i][sz] = min(dp[i + 1][sz - 1], dp[i][sz - 1]) + 1

print(dp[0][n])

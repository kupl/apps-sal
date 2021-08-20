(n, p, q, r) = [int(i) for i in input().split(' ')]
a = input()
b = a.split()
for i in range(n):
    b[i] = int(b[i])
dp = [p * b[0]]
for i in range(1, n):
    dp.append(max(dp[i - 1], p * b[i]))
dq = [dp[0] + q * b[0]]
for i in range(1, n):
    dq.append(max(dq[i - 1], dp[i] + q * b[i]))
dr = [dq[0] + r * b[0]]
for i in range(1, n):
    dr.append(max(dr[i - 1], dq[i] + r * b[i]))
print(dr[-1])

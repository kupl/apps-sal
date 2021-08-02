n, m = list(map(int, input().split()))
x = 2**n
dp = [1000000000 for _ in range(x)]
dp[0] = 0
for i in range(m):
    ai, bi = list(map(int, input().split()))
    c = list(map(int, input().split()))
    bit = 0
    for j in range(bi):
        bit += 2**(c[j] - 1)
    for k in range(x):
        dp[k | bit] = min(dp[k | bit], dp[k] + ai)
if dp[x - 1] == 1000000000:
    print((-1))
else:
    print((dp[x - 1]))

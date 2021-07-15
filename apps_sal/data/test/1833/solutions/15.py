n = int(input())
a = list(map(int, input().split()))
N = 1000005
MOD = 10 ** 9 + 7
dp =[0] * N
dp[0] = 0
for i in range(n):
    cur = []
    A = int(a[i] ** 0.5) + 1
    for j in range(1, A):
        if a[i] % j == 0:
            cur.append(j)
            if a[i] // j != j:
                cur.append(a[i] // j)

    cur = sorted(cur, reverse=True)
    for j in cur:
        if j == 1:
            dp[j] += 1
        else:
            dp[j] += dp[j - 1]

ans = 0
for i in dp:
    ans += i
    ans %= MOD
print(ans)


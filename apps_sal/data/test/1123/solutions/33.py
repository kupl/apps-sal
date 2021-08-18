
MOD = 10 ** 9 + 7

n, k = list(map(int, input().split()))
dic = [0] * (k + 1)

ans = 0
for i in range(k, 0, -1):
    dic[i] = pow(k // i, n, MOD)

for i in range(k, 0, -1):
    for j in range(i * 2, k + 1, i):
        dic[i] -= dic[j]
        dic[i] %= MOD

ans = 0
for i in range(1, k + 1):
    ans += dic[i] * i
    ans %= MOD

print(ans)

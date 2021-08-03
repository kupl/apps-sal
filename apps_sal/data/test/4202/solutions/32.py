L, R = map(int, input().split())

MOD = 2019

ans = 2020**2

if R - L >= 2020:
    print(0)
else:
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            ans = min(ans, i % MOD * j % MOD)
    print(ans)

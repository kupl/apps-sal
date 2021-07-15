c, d = list(map(int, input().split(' ')))
n, m = list(map(int, input().split(' ')))
k = int(input())
dp = [0] * 100000
need = n*m - k

if need <= 0:
    print(0)
    quit()


for i in range(1, 100000):
    dp[i] = min(dp[i-n]+c, dp[i-1]+d)

print(dp[need])


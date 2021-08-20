MOD = 10 ** 9 + 7
N = int(input())
AN = list(map(int, input().split()))
cumsum = [0] * (len(AN) + 1)
for i in range(1, N + 1):
    cumsum[i] = cumsum[i - 1] + AN[i - 1]
ans = 0
for i in range(1, N):
    ans += AN[i] * cumsum[i]
    ans %= MOD
print(ans)

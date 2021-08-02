MOD = 1000000007

N = int(input())
C = list(map(int, input().split()))

C.sort(reverse=True)

ans = 0

for i in range(N):
    ans += C[i] * (2 + i) * pow(4, N - 1, MOD)
    ans %= MOD

print(ans)

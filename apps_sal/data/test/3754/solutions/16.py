N = int(input())
D = list(map(int, input().strip().split()))
MOD = 998244353
ans = 1
for d in D:
    ans *= d
    ans %= MOD
dsum = sum(D) - N
for i in range(N - 2):
    ans *= dsum - i
    ans %= MOD
print(ans)

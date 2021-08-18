N = int(input())
M = 10**9 + 7
A = list(map(int, input().split()))

ans = 0
for i in range(60):
    one = sum([a >> i & 1 for a in A])
    zero = N - one
    ans += (one * zero) * 2**i
    ans %= M
print(ans)

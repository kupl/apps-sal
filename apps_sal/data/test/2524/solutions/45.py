N = int(input())
M = 10**9 + 7
A = [int(x) for x in input().split()]

ans = 0
for i in range(60):
    one = sum([a >> i & 1 for a in A])
    zero = N - one
    ans += (one * zero) * pow(2, i, M) % M
    ans %= M
print(ans)

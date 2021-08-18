N = int(input())
M = 10**9 + 7
A = [int(x) for x in input().split()]

ans = p = 0
for i in range(60):
    one = sum([a >> p & 1 for a in A])
    zero = N - one
    p += 1
    ans += (one * zero) * 2**i
    ans %= M
print(ans)

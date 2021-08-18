MOD = 10**9 + 7

N = int(input())
C = list(map(int, input().split()))

C.sort(reverse=True)
ans = 0

if N == 1:
    ans = C[0] * 2**N
else:
    for i in range(N):
        ans += C[i] * (2 + i)

    ans *= 4**(N - 1)

print((ans % MOD))

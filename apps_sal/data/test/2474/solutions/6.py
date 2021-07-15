MOD = 10**9 + 7

N = int(input())
Cs = list(map(int, input().split()))

Cs.sort(reverse=True)

pow2 = pow(2, 2*N-2, MOD)

ans = 0
for i, C in enumerate(Cs, start=1):
    ans += C*(i+1)*pow2
    ans %= MOD

print(ans)


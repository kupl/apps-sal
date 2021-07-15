import sys
input = sys.stdin.readline

mod = 10**9 + 7
N = int(input())
AA, AB, BA, BB = [input().rstrip() for _ in range(4)]

if N <= 3:
    print(1)
    return

fact = [1] * (N+1)
fact_inv = [1] * (N+1)
for i in range(1, N+1):
    fact[i] = i * fact[i-1] % mod
fact_inv[N] = pow(fact[N], mod-2, mod)
for i in range(1, N+1)[::-1]:
    fact_inv[i-1] = i * fact_inv[i] % mod
comb = lambda n, k: fact[n] * fact_inv[k] * fact_inv[n-k] % mod

if AB == 'A':
    if AA == 'A':
        print(1)
    else:
        if BA == 'A':
            ans = 0
            for x in range(N - 3 + 1):
                if N - 3 - x + 1 < x:
                    break
                ans = (ans + comb(N - 3 - x + 1, x)) % mod
            print(ans)
        else:
            print(pow(2, N - 3, mod))
else:
    if BB == 'B':
        print(1)
    else:
        if BA == 'B':
            ans = 0
            for x in range(N - 3 + 1):
                if N - 3 - x + 1 < x:
                    break
                ans = (ans + comb(N - 3 - x + 1, x)) % mod
            print(ans)
        else:
            print(pow(2, N - 3, mod))

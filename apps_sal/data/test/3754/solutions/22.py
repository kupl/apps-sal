mod = 998244353

N, *D = map(int, open(0).read().split())

ans = 1
for d in D:
    ans = ans * d % mod

S = sum(D)
for i in range(N - 2):
    ans = ans * (S - N - i) % mod

print(ans)

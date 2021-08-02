def nCk(_n, _k):
    return (fact[_n] // (fact[_k] * fact[_n - _k])) % m


fact = [1] * 2005
for i in range(1, 2004):
    fact[i] = fact[i - 1] * i

n, k = list(map(int, input().split()))
r = n - k
m = 10**9 + 7

for i in range(1, k + 1):
    if r < i - 1: print((0)); continue;
    if i == 1: print((r + i)); continue;
    else:
        ans = nCk(r + 1, i) * nCk(k - 1, i - 1)
        print((ans % m))

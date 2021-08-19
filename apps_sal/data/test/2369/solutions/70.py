def calc(x, y):
    a = fac[x]
    b = fac[y]
    c = fac[x - y]
    ret = a % p * pow(b, p - 2, p) * pow(c, p - 2, p) % p
    return ret


(N, K) = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
p = 10 ** 9 + 7
fac = [1]
for i in range(1, N + 1):
    fac.append(fac[-1] * i % p)
ans = 0
for i in range(N):
    if i <= N - K:
        nokori = N - 1 - i
        kumi = calc(nokori, K - 1)
        ans -= A[i] * kumi % p
    if i >= K - 1:
        nokori = i
        kumi = calc(nokori, K - 1)
        ans += A[i] * kumi % p
print(ans % p)

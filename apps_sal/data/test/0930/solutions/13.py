P = 10 ** 9 + 7
N = 700000
inv = [0] + [1]
finv = [1] + [1]
fac = [1] + [1]
for i in range(2, N + 1):
    inv += [inv[P % i] * (P - int(P / i)) % P]
    fac += [fac[i - 1] * i % P]
    finv += [finv[i - 1] * inv[i] % P]


def comb(a, b):
    if a < b:
        return 0
    return fac[a] * (finv[b] * finv[a - b] % P) % P


(n, k) = list(map(int, input().split()))
ans = 0
num = min(n - 1, k) + 1
for i in range(num):
    heya = n - i
    ret = comb(n, i)
    person = n - heya
    ret = ret * comb(person + heya - 1, person) % P
    ans += ret
print(ans % P)

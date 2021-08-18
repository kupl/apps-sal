def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7
N = 2 * 10**5
g1 = [1] * (N + 1)
g2 = [1] * (N + 1)
inverse = [1] * (N + 1)

for i in range(2, N + 1):
    g1[i] = ((g1[i - 1] * i) % mod)
    inverse[i] = ((-inverse[mod % i] * (mod // i)) % mod)
    g2[i] = ((g2[i - 1] * inverse[i]) % mod)
inverse[0] = 0

N = int(input())
aa = input()
ab = input()
ba = input()
bb = input()

if ab == "A":
    if aa == "A":
        print(1)
    else:
        if ba == "A":
            res = 0
            for k in range(1, N // 2 + 1):
                tmp = N - 1 - (2 * k - 1)
                res += cmb(tmp + k - 1, k - 1, mod)
                res %= mod
            print(res)
        else:
            res = 0
            for k in range(1, N // 2 + 1):
                tmp = N - 1 - (2 * k - 1)
                res += cmb(tmp + 2 * k - 2, 2 * k - 2, mod)
                res %= mod
            print(res)
else:
    if bb == "B":
        print(1)
    else:
        if ba == "B":
            res = 0
            for k in range(1, N // 2 + 1):
                tmp = N - 1 - (2 * k - 1)
                res += cmb(tmp + k - 1, k - 1, mod)
                res %= mod
            print(res)
        else:
            res = 0
            for k in range(1, N // 2 + 1):
                tmp = N - 1 - (2 * k - 1)
                res += cmb(tmp + 2 * k - 2, 2 * k - 2, mod)
                res %= mod
            print(res)

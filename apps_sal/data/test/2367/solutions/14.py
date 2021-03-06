def ext_euclid(a, b):
    if b == 0:
        return (1, 0, a)
    (y, x, v) = ext_euclid(b, a % b)
    y -= a // b * x
    return (x, y, v)


def mod_inv(a, mod):
    (x, _, _) = ext_euclid(a, mod)
    return x % mod


def comb_list_1(H, W, A, B, mod, modinv_list):
    ret = [0 for _ in range(H - A)]
    c = 1
    for h in range(H - A):
        ret[h] = c
        c *= h + B
        c *= modinv_list[h + 1]
        c %= mod
    return ret


def comb_list_2(H, W, A, B, mod, modinv_list):
    ret = [0 for _ in range(H - A)]
    c = 1
    for a in range(1, A + 1):
        c *= a + W - B - 1
        c *= modinv_list[a]
        c %= mod
    for h in range(H - A - 1, -1, -1):
        ret[h] = c
        c *= H - h + W - B - 1
        c *= modinv_list[H - h]
        c %= mod
    return ret


def main():
    MOD = 10 ** 9 + 7
    (H, W, A, B) = list(map(int, input().split(' ')))
    modinv_list = [None] + [mod_inv(h, MOD) for h in range(1, H + 1)]
    combs_1 = comb_list_1(H, W, A, B, MOD, modinv_list)
    combs_2 = comb_list_2(H, W, A, B, MOD, modinv_list)
    ans = 0
    for (c1, c2) in zip(combs_1, combs_2):
        ans += c1 * c2
        ans %= MOD
    print(ans)


def __starting_point():
    main()


__starting_point()

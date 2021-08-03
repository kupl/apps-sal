def main():
    K = int(input())
    S = input()
    N = len(S)
    mod = 10**9 + 7
    r = 0
    t = pow(26, K, mod)
    s = 1
    inv26 = pow(26, mod - 2, mod)
    inv = [0] * (K + 2)
    inv[1] = 1
    for i in range(2, K + 2):
        inv[i] = -inv[mod % i] * (mod // i) % mod
    for i in range(K + 1):
        r = (r + t * s) % mod
        t = (t * 25 * inv26) % mod
        s = (s * (N + i) * inv[i + 1]) % mod
    return r


print((main()))

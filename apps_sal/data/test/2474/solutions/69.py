def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    mod = 10 ** 9 + 7
    r = 0
    n = N
    i = 0
    for c in C:
        if n == 1:
            r = (r + c * pow(2, N - 1, mod)) % mod
        else:
            r = (r + c * (n + 1) * pow(2, n - 2, mod) * pow(2, N - n, mod)) % mod
        n -= 1
    return 2**N * r % mod


print((main()))

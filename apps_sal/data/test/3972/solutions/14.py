def main():
    mod = 10**9 + 7
    n = int(input())
    a, b, c, p = 1, 1, n, n - 1
    for i in range(n - 1):
        p = (p + a - 1) % mod
        a, b, c = b, c, ((n - 1) * (n - 1) + p + c) % mod
    print(c)


main()

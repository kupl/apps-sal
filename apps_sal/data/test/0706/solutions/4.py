def main():
    mod = 1000000007
    (a, b, n, x) = list(map(int, input().split()))
    if a == 1:
        print((x + n * b) % mod)
    else:
        print(((pow(a, n, mod) - 1) * pow(a - 1, mod - 2, mod) * b + pow(a, n, mod) * x) % mod)


main()

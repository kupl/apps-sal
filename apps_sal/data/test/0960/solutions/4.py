def main():
    (n, k) = list(map(int, input().split()))
    x = float('+inf')
    for r in range(1, k):
        if n % r != 0:
            continue
        q = n // r
        x = min(x, q * k + r)
    print(x)


main()

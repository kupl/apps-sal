def main():
    from math import factorial

    n, m = map(int, input().split())
    p = 10**9 + 7

    if abs(n - m) < 2:
        if n == m:
            print(2 * factorial(n) * factorial(m) % p)
        else:
            print(factorial(n) * factorial(m) % p)
    else:
        print(0)


if __name__ == "__main__":
    main()

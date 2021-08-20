def main():
    (n, m) = map(int, input().split())
    if m > n:
        (n, m) = (m, n)
    if n + m <= 4:
        print(0)
        return
    if m == 1:
        q = n // 6
        r = n % 6
        if r == 4:
            print(n - 2)
        elif r == 5:
            print(n - 1)
        else:
            print(q * 6)
        return
    if (n, m) in [(7, 2), (3, 2)]:
        print(n * m - 2)
        return
    if n % 2 == 0 or m % 2 == 0:
        print(n * m)
        return
    print(n * m - 1)


main()

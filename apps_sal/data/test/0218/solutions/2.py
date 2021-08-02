def main():
    items = input().split()
    n = int(items[0])
    p = int(items[1])
    q = int(items[2])
    s = input()
    A = int(n / p)
    for a in range(A + 1):
        forq = n - a * p
        if forq % q == 0:
            b = int(forq / q)
            print(a + b)
            for i in range(a):
                print(s[i * p:(i + 1) * p])
            for i in range(b):
                print(s[a * p + i * q:a * p + (i + 1) * q])
            return
    print(-1)


def __starting_point():
    main()


__starting_point()

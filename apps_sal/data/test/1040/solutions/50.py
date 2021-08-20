def main():
    n = int(input())
    s = str(input())
    num = len(s)
    n = 0
    while True:
        if n + 3 > num:
            break
        if s[n:n + 3] == 'fox':
            s = s[:n] + s[n + 3:]
            n = max(0, n - 3)
        else:
            n += 1
    print(len(s))


def __starting_point():
    main()


__starting_point()

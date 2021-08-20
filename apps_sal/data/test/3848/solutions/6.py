def main():
    (n, p) = list(map(int, input().split()))
    l = [p, p] + [ord(c) - 97 for c in input()]
    a = l[-2]
    for i in range(n + 1, 1, -1):
        (a, b) = (l[i - 2], a)
        for x in range(l[i] + 1, p):
            if a != x != b:
                l[i] = x
                break
        else:
            continue
        break
    else:
        print('NO')
        return
    (a, b) = (l[i - 1], x)
    for i in range(i + 1, n + 2):
        for x in range(p):
            if a != x != b:
                l[i] = x
                (a, b) = (b, x)
                break
    print(''.join((chr(x + 97) for x in l[2:])))


def __starting_point():
    main()


__starting_point()

def NOD(x, y):
    while (y != 0):
        x = x % y
        x, y = y, x
    return x


def main():
    l, r = map(int, input().split())
    for a in range(l, r - 1):
        for b in range(a, r):
            for c in range(b, r + 1):
                if NOD(a, b) == 1 and NOD(b, c) == 1 and NOD(a, c) != 1:
                    print(a, b, c)
                    return
    print(-1)


main()

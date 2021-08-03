X, N = list(map(int, input().split()))
p = list(map(int, input().split()))

p.sort()


def main():

    if len(p) == 0:
        print(X)
        return

    if X < p[0] and p[-1] < X:
        print(X)

    keep = True
    i = 0
    while keep:
        left_found = (X - i) not in p
        right_found = (X + i) not in p

        if left_found and right_found:
            print((X - i))
            keep = False
        elif left_found:
            print((X - i))
            keep = False
        elif right_found:
            print((X + i))
            keep = False

        i += 1


def __starting_point():
    main()


__starting_point()

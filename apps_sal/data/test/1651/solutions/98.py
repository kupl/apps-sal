def main():
    import sys
    input = sys.stdin.readline
    (S, P) = [int(x) for x in input().strip().split()]
    for i in range(1, int(P ** 0.5) + 1):
        if P % i > 0:
            continue
        if i + P // i == S:
            print('Yes')
            return True
    else:
        print('No')


def __starting_point():
    main()


__starting_point()

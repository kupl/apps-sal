def main():
    import sys
    from bisect import bisect
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    n = int(input())
    cc = sorted(map(int, input().split()))
    print(n - max((bisect(cc, c * 2, i) - i for (i, c) in enumerate(cc))))


def __starting_point():
    main()


__starting_point()

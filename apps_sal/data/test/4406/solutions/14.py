import sys


def main():
    def input():
        return sys.stdin.readline()[:-1]

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    l = []
    for e in a:
        if len(l) == k:
            if e not in l:
                l = [e] + l[:-1]
            else:
                pass
        else:
            if e not in l:
                l = [e] + l
            else:
                pass
    print(len(l))
    print(*l, sep=" ")


def __starting_point():
    main()


__starting_point()

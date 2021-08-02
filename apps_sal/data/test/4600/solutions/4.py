import sys


def readint():
    return int(sys.stdin.readline())


def readints():
    return tuple(map(int, sys.stdin.readline().split()))


def readintslist(n):
    return [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]


def main():
    n, m = readints()
    frag = [False] * (n + 1)
    penalties = [0] * (n + 1)
    for _ in range(m):
        p, s = input().split()
        p = int(p)
        if frag[p]:
            continue
        if s == "AC":
            frag[p] = True
        else:
            penalties[p] += 1
    print(sum(frag), sum([penalties[i] for i in range(n + 1) if frag[i]]))


def __starting_point():
    main()


__starting_point()

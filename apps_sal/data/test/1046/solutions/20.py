from collections import Counter


def main():
    n = int(input())
    d = Counter(list(map(int, input().split())))
    d[0] = 0
    if max(d.values()) < 3:
        print(Counter(list(d.values()))[2])
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()

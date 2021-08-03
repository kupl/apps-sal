from collections import Counter


def main():
    S = input()
    cs = Counter(S)
    ans = min(cs['0'], cs['1']) * 2
    print(ans)


def __starting_point():
    main()


__starting_point()

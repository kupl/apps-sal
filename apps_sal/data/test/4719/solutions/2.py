
from collections import Counter


def solve(n, a):
    alphabetLst = {}
    for i in range(n):
        d = Counter(a[i])
        for c in (chr(ord("a") + i) for i in range(26)):
            if not c in d.keys():
                alphabetLst[c] = 0
            elif not c in alphabetLst.keys():
                alphabetLst[c] = d[c]
            elif d[c] < alphabetLst[c]:
                alphabetLst[c] = d[c]

    res = []
    for k, v in alphabetLst.items():
        res += [k] * v

    return "".join(res)


def main():
    N = int(input())
    a = [input() for _ in range(N)]
    print(solve(N, a))
    return


def __starting_point():
    main()


__starting_point()

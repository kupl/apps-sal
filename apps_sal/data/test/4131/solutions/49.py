import sys
from operator import itemgetter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *PY = map(int, read().split())
    city = [(p, y, i) for i, (p, y) in enumerate(zip(*[iter(PY)] * 2))]

    city.sort(key=itemgetter(1))

    counter = [0] * (N + 1)
    ans = [0] * M
    for p, y, i in city:
        counter[p] += 1
        ans[i] = f"{p:>06}{counter[p]:>06}"

    print(*ans, sep='\n')

    return


def __starting_point():
    main()


__starting_point()

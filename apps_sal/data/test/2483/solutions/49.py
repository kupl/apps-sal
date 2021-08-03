import sys

input = sys.stdin.readline


def main():
    N, C = [int(x) for x in input().split()]
    STC = [[int(x) for x in input().split()] for _ in range(N)]

    S = [[] for _ in range(10 ** 5 + 1)]
    T = [[] for _ in range(10 ** 5 + 1)]

    for s, t, c in STC:
        S[s].append(c)
        T[t].append(c)

    used = set()
    ans = 0
    for i in range(10 ** 5 + 1):
        sused = set()
        tused = set()

        for s in S[i]:
            sused.add(s)
        for t in T[i]:
            tused.add(t)

        ans = max(ans, len(used) + len(sused - tused))
        used = used - tused | sused

    print(ans)


def __starting_point():
    main()


__starting_point()

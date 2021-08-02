import sys
sys.setrecursionlimit(100000000)


def main():
    S = input()
    N = len(S)
    ans = 0
    before = 0
    for i in range(N - 1):
        if S[i] != S[i + 1]:
            ans = max(ans, min(N - before, i + 1))
            before = i + 1
    ans = max(ans, N - before)
    print(ans)


def __starting_point():
    main()


__starting_point()

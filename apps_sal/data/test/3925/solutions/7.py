3


def solve(S):
    N = len(S)
    lens = []
    start = 0
    for i in range(1, N):
        if S[i] == S[i - 1]:
            lens.append(i - start)
            start = i
    lens.append(N - start)
    best = max(lens)
    if S[0] != S[-1] and len(lens) > 1:
        best = max(best, lens[0] + lens[-1])
    return best


def main():
    S = input()
    print(solve(S))


def __starting_point():
    main()


__starting_point()

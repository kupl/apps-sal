def solve(S):
    import math
    N = len(S)
    ans = [0] * N
    L = 0
    R = 0
    for i in range(N - 1):
        if S[i] == 'R':
            R += 1
        if S[i + 1] == 'L' and R > 0:
            ans[i] += math.ceil(R / 2)
            ans[i + 1] += math.floor(R / 2)
            R = 0
        if S[N - (i + 1)] == 'L':
            L += 1
        if S[N - (i + 1) - 1] == 'R' and L > 0:
            ans[N - (i + 1)] += math.ceil(L / 2)
            ans[N - (i + 1) - 1] += math.floor(L / 2)
            L = 0
    print(' '.join([str(i) for i in ans]))


def __starting_point():
    S = input()
    solve(S)


__starting_point()

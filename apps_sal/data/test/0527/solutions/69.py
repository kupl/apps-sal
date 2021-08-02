import sys
from string import ascii_lowercase as a2z

input = sys.stdin.readline


def main():
    S = input().rstrip()
    T = input().rstrip()

    N = len(S)
    memo = [None] * N
    memo[-1] = {alphabet: -1 for alphabet in a2z}
    memo[-1][S[-1]] = N - 1
    for i in reversed(list(range(N - 1))):
        memo[i] = memo[i + 1].copy()
        memo[i][S[i]] = i

    ans = 0
    idx_S = 0
    for t in T:
        i = memo[idx_S][t]
        if i == -1:
            ans += (N - idx_S)
            idx_S = 0
            i = memo[idx_S][t]
            if i == -1:
                ans = -1
                break
            else:
                ans += i - idx_S + 1
                if i == N - 1:
                    idx_S = 0
                else:
                    idx_S = i + 1
        else:
            ans += i - idx_S + 1
            if i == N - 1:
                idx_S = 0
            else:
                idx_S = i + 1

    print(ans)


def __starting_point():
    main()


__starting_point()

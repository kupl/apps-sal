import sys
import collections

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 5)


def solve(S, ans, N):
    f = False
    ff = False
    for i in range(1, N):
        if i == N - 1:
            if S[i] == "o" and ans[i] == "S":
                if ans[i - 1] == ans[0]:
                    f = True
            if S[i] == "o" and ans[i] == "W":
                if ans[i - 1] != ans[0]:
                    f = True
            if S[i] == "x" and ans[i] == "S":
                if ans[i - 1] != ans[0]:
                    f = True
            if S[i] == "x" and ans[i] == "W":
                if ans[i - 1] == ans[0]:
                    f = True
        elif i == N - 2:
            if S[i] == "o" and ans[i] == "S":
                if ans[i - 1] == ans[i + 1]:
                    ff = True
            if S[i] == "o" and ans[i] == "W":
                if ans[i - 1] != ans[i + 1]:
                    ff = True
            if S[i] == "x" and ans[i] == "S":
                if ans[i - 1] != ans[i + 1]:
                    ff = True
            if S[i] == "x" and ans[i] == "W":
                if ans[i - 1] == ans[i + 1]:
                    ff = True
        else:
            if S[i] == "o" and ans[i] == "S":
                ans[i + 1] = ans[i - 1]
            if S[i] == "o" and ans[i] == "W":
                if ans[i - 1] == "S":
                    ans[i + 1] = "W"
                else:
                    ans[i + 1] = "S"
            if S[i] == "x" and ans[i] == "S":
                if ans[i - 1] == "S":
                    ans[i + 1] = "W"
                else:
                    ans[i + 1] = "S"
            if S[i] == "x" and ans[i] == "W":
                ans[i + 1] = ans[i - 1]

    return f and ff, ans


def main():
    N = int(input())
    S = input().strip()

    ans = [""] * N
    ans[0] = "S"
    if S[0] == "o":
        ans[-1] = "S"
        ans[1] = "S"
    else:
        ans[-1] = "S"
        ans[1] = "W"
    f, ans = solve(S, ans, N)
    if f:
        print(("".join(ans)))
        return

    ans = [""] * N
    ans[0] = "S"
    if S[0] == "o":
        ans[-1] = "W"
        ans[1] = "W"
    else:
        ans[-1] = "W"
        ans[1] = "S"
    f, ans = solve(S, ans, N)
    if f:
        print(("".join(ans)))
        return

    ans = [""] * N
    ans[0] = "W"
    if S[0] == "o":
        ans[-1] = "S"
        ans[1] = "W"
    else:
        ans[-1] = "S"
        ans[1] = "S"
    f, ans = solve(S, ans, N)
    if f:
        print(("".join(ans)))
        return

    ans = [""] * N
    ans[0] = "W"
    if S[0] == "o":
        ans[-1] = "W"
        ans[1] = "S"
    else:
        ans[-1] = "W"
        ans[1] = "W"
    f, ans = solve(S, ans, N)
    if f:
        print(("".join(ans)))
        return

    print((-1))


def __starting_point():
    main()


__starting_point()

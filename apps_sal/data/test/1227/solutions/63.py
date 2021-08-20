import sys
input = sys.stdin.readline


def solve_K_1(N):
    S = str(N)
    d = len(S)
    return 9 * (d - 1) + int(S[0])


def solve_K_2(N):
    if N <= 99:
        return N - solve_K_1(N)
    S = str(N)
    d = len(S)
    res = 0
    res += 81 * (d - 1) * (d - 2) // 2
    res += 9 * (d - 1) * (int(S[0]) - 1)
    x = 0
    for i in range(1, d):
        if S[i] != '0':
            x = int(S[i])
            break
    i += 1
    res += x + 9 * (d - i)
    return res


def solve_K_3(N):
    if N <= 999:
        return N - solve_K_1(N) - solve_K_2(N)
    S = str(N)
    d = len(S)
    res = 0
    for n in range(3, d):
        res += 729 * (n - 1) * (n - 2) // 2
    res += 81 * (d - 1) * (d - 2) // 2 * (int(S[0]) - 1)
    res += solve_K_2(int(S[1:]))
    return res


def main():
    N = int(input())
    K = int(input())
    if K == 1:
        ans = solve_K_1(N)
    elif K == 2:
        ans = solve_K_2(N)
    elif K == 3:
        ans = solve_K_3(N)
    print(ans)


def __starting_point():
    main()


__starting_point()

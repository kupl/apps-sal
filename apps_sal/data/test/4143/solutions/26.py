def solve(N, A, B, C, D, E):
    tmp = min(A, B, C, D, E)
    (tmp, tmp2) = divmod(N, tmp)
    tmp += 0 if tmp2 == 0 else 1
    print(tmp + 4)


def __starting_point():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    solve(N, A, B, C, D, E)


__starting_point()

import random


def solve(N, P):
    operation = []
    target = 1
    confirmed_start = 0
    confirmed_end = -1
    for i in range(N):
        if P[i] == target:
            for j in range(i - 1, confirmed_start - 1, -1):
                (P[j], P[j + 1]) = (P[j + 1], P[j])
                operation.append(j + 1)
            confirmed_end = i
            for j in range(confirmed_start, confirmed_end):
                if P[j] != j + 1:
                    print(-1)
                    return
            target = i + 1
            confirmed_start = confirmed_end
    if confirmed_end != N - 1:
        print(-1)
        return
    print(*operation, sep='\n')


def __starting_point():
    N = int(input())
    P = list(map(int, input().split()))
    solve(N, P)


__starting_point()

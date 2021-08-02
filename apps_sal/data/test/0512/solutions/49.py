import sys
from typing import List

sys.setrecursionlimit(10 ** 9)


def lmi():
    return list(map(int, input().split()))


def main():
    N = int(input())
    AB = [lmi() for _ in range(N)]
    result = solve(N, AB)
    print(result)


def solve(N: int, AB: List[List[int]]) -> str:
    for a, b in AB:
        if a != -1 and b != -1 and not a < b:
            return 'No'
    exists = [False] * (2 * N + 1)
    for a, b in AB:
        if a != -1:
            if exists[a]:
                return 'No'
            exists[a] = True
        if b != -1:
            if exists[b]:
                return 'No'
            exists[b] = True
    P = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]
    for a, b in AB:
        if a != -1:
            for i in range(1, a):
                P[i][a] = -1
            for i in range(a + 1, 2 * N + 1):
                if exists[i]:
                    P[a][i] = -1
        if b != -1:
            for i in range(b + 1, 2 * N + 1):
                P[b][i] = -1
            for j in range(0, b):
                if exists[j]:
                    P[j][b] = -1
        if a != -1 and b != -1:
            for i in range(0, a):
                for j in range(b + 1, 2 * N + 1):
                    P[i][j] = -1
            for i in range(a + 1, b):
                for j in range(i, b):
                    P[i][j] = -1
            P[a][b] = 0

    dp = [False] * (2 * N + 1)
    dp[0] = True
    for i in range(0, 2 * N + 1, 2):
        if dp[i]:
            for j in range(i + 2, 2 * N + 1, 2):
                ng = False
                step = (j - i) // 2
                for k in range(step):
                    a = i + 1 + k
                    b = a + step
                    if P[a][b] == -1:
                        ng = True
                        break
                if not ng:
                    dp[j] = True

    return 'Yes' if dp[2 * N] else 'No'


def __starting_point():
    main()


__starting_point()

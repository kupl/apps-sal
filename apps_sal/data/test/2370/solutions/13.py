import sys
import numpy as np


def main():
    input = sys.stdin.readline
    N = int(input())
    A = np.array([list(map(int, input().split())) for i in range(N)])
    INF = 10 ** 10
    for i in range(N):
        A[i][i] = INF
    ans = 0
    for i in range(N):
        for j in range(i):
            bipas = np.min(A[i] + A[j])
            if A[i][j] > bipas:
                print(-1)
                return 0
            elif A[i][j] < bipas:
                ans += A[i][j]
    print(ans)


def __starting_point():
    main()


__starting_point()

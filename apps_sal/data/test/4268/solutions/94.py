# coding: utf-8
from math import sqrt

def main():
    N, D = list(map(int, input().split()))
    ans = 0
    X = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N - 1):
        for j in range(i + 1, N):
            tmp = sum([(X[i][k] - X[j][k]) ** 2 for k in range(D)])
            if tmp == int(sqrt(tmp)) ** 2:
                ans += 1

    print(ans)

def __starting_point():
    main()

__starting_point()

import sys
import numpy as np


def main():
    (N, Q) = list(map(int, sys.stdin.readline().rstrip().split()))
    H = np.array([0] * (N - 1))
    W = np.array([0] * (N - 1))
    black = (N - 2) ** 2
    Hmin = N - 1
    Wmin = N - 1
    for i in range(Q):
        (n, x) = list(map(int, sys.stdin.readline().rstrip().split()))
        if n == 1:
            if x - 1 <= Wmin:
                W[x - 1:Wmin] = Hmin - 1
                Wmin = x - 1
            black -= W[x - 1]
        else:
            if x - 1 <= Hmin:
                H[x - 1:Hmin] = Wmin - 1
                Hmin = x - 1
            black -= H[x - 1]
    print(black)


main()

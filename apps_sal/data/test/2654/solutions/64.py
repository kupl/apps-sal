import sys
import numpy as np
input = sys.stdin.readline
read = sys.stdin.read


def log(*args):
    print(*args, file=sys.stderr)


def main():
    np.set_printoptions(threshold=20)
    N = int(input())
    AB = np.array(read().split(), dtype=np.int)
    A = AB[0::2]
    B = AB[1::2]
    A.sort()
    B.sort()
    if N % 2 == 1:
        n = N // 2
        print(B[n] - A[n] + 1)
    else:
        n = N // 2
        print((B[n] + B[n - 1]) - (A[n] + A[n - 1]) + 1)


def __starting_point():
    main()


__starting_point()

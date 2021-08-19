import math
import numpy as np
import sys
input = sys.stdin.readline
mod = 1000000007


def main():
    n = int(input())
    A = list(map(int, input().split()))
    for i in range(n):
        A[i] -= i + 1
    b = int(np.median(A))
    for i in range(n):
        A[i] = abs(A[i] - b)
    print(int(np.sum(A)))


main()

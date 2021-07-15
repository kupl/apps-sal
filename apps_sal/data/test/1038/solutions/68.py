import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    A, B = NMI()
    C = [[0]*2 for _ in range(42)]
    B = B + 1
    for i in range(42):
        tmp = B - (B // (2**(i+1))) * 2**(i+1)
        if tmp < 2**i:
            C[i][0] = tmp + (B // (2**(i+1))) * 2**i
            C[i][1] = (B // (2 ** (i + 1))) * 2 ** i
        else:
            C[i][0] = 2**i + (B // (2**(i+1))) * 2**i
            C[i][1] = tmp - 2**i + (B // (2**(i+1))) * 2**i


    B = A
    for i in range(42):
        tmp = B - (B // (2**(i+1))) * 2**(i+1)
        if tmp < 2**i:
            C[i][0] -= tmp + (B // (2**(i+1))) * 2**i
            C[i][1] -= (B // (2 ** (i + 1))) * 2 ** i
        else:
            C[i][0] -= 2**i + (B // (2**(i+1))) * 2**i
            C[i][1] -= tmp - 2**i + (B // (2**(i+1))) * 2**i
    ans = 0
    for i in range(42):
        ans += C[i][1] % 2 * 2**i
    print(ans)


def __starting_point():
    main()
__starting_point()

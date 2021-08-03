from itertools import accumulate
from collections import defaultdict
import sys
input = sys.stdin.readline


def read():
    N, M = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))
    return N, M, A


def solve(N, M, A):
    D = defaultdict(int)
    S = [0 for i in range(N + 1)]
    for i in range(N):
        s = (S[i] + A[i]) % M
        S[i + 1] = s
        D[s] += 1
    ans = 0
    k = 0
    for i in range(N):
        ans += D[k]
        k += A[i]
        k %= M
        D[k] -= 1
    return ans


def __starting_point():
    inputs = read()
    print((solve(*inputs)))


__starting_point()

import sys
from collections import Counter


def input():
    return sys.stdin.readline()[:-1]


def main():
    (N, M) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    S = [0] * N
    S[0] = A[0] % M
    for k in range(1, N):
        S[k] = (S[k - 1] + A[k]) % M
    C = Counter(S)
    C[0] += 1
    ans = 0
    for e in C:
        ans += C[e] * (C[e] - 1) // 2
    print(ans)


def __starting_point():
    main()


__starting_point()

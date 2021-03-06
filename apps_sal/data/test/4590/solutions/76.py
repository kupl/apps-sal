from itertools import accumulate
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    (n, m, k) = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))
    A = list(accumulate(A))
    B = list(accumulate(B))
    ans = 0
    j = m
    for i in range(n + 1):
        if A[i] > k:
            break
        while A[i] + B[j] > k:
            j -= 1
        ans = max(ans, i + j)
    print(ans)


def __starting_point():
    main()


__starting_point()

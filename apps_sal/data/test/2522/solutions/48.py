import sys
import collections

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    ac = collections.Counter(A)
    bc = collections.Counter(B)

    for i in range(1, N + 1):
        if ac[i] + bc[i] > N:
            print("No")
            return

    ma = 0
    cnta = 0
    cntb = 0
    for i in range(1, N + 1):
        cnta += ac[i]
        cntb += bc[i - 1]
        ma = max(ma, cnta - cntb)

    print("Yes")
    ans = []
    for i in range(N):
        ans.append(B[(i + N - ma) % N])
    print((*ans))


def __starting_point():
    main()

__starting_point()

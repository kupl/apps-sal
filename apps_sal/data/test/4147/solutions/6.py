import sys
from itertools import product

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = list(map(int, readline().split()))
    (*L,) = list(map(int, read().split()))

    ans = INF
    for p in product(list(range(4)), repeat=N):
        num = [0] * 3
        length = [0] * 3
        for i, j in enumerate(p):
            if j < 3:
                num[j] += 1
                length[j] += L[i]
        res = 0
        for j in range(3):
            if num[j] == 0:
                res = INF
                break
            else:
                res += (num[j] - 1) * 10 + abs(length[j] - A[j])
        if ans > res:
            ans = res

    print(ans)
    return


def __starting_point():
    main()

__starting_point()

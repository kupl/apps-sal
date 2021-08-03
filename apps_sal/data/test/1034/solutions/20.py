import sys
from heapq import heappop, heappush

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    X, Y, Z, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))
    C = list(map(int, readline().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    hq = [(-(A[0] + B[0] + C[0]), 0, 0, 0)]

    ans = [0] * K
    added = {(0, 0, 0)}

    for idx in range(K):
        taste, i, j, k = heappop(hq)
        ans[idx] = -taste
        if i < X - 1 and (i + 1, j, k) not in added:
            heappush(hq, (-(A[i + 1] + B[j] + C[k]), i + 1, j, k))
            added.add((i + 1, j, k))
        if j < Y - 1 and (i, j + 1, k) not in added:
            heappush(hq, (-(A[i] + B[j + 1] + C[k]), i, j + 1, k))
            added.add((i, j + 1, k))
        if k < Z - 1 and (i, j, k + 1) not in added:
            heappush(hq, (-(A[i] + B[j] + C[k + 1]), i, j, k + 1))
            added.add((i, j, k + 1))

    print(*ans, sep='\n')
    return


def __starting_point():
    main()


__starting_point()

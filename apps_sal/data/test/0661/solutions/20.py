import sys
from itertools import permutations
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (M, K) = list(map(int, readline().split()))
    if M == 0:
        if K == 0:
            print((0, 0))
            return
        else:
            print(-1)
            return
    elif M == 1:
        if K == 0:
            print((0, 0, 1, 1))
            return
        else:
            print(-1)
            return
    elif K >= pow(2, M):
        print(-1)
        return
    vec = [i for i in range(pow(2, M)) if i != K]
    ans = vec + [K] + vec[::-1] + [K]
    print(' '.join(map(str, ans)))
    return


def __starting_point():
    main()


__starting_point()

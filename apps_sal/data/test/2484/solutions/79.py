import sys


def input():
    return sys.stdin.readline().strip()


MOD = 10 ** 9 + 7
sys.setrecursionlimit(20000000)
INF = float('inf')


def main():
    N = int(input())
    A = list(map(int, input().split()))
    (right, ans, tmp) = (0, 0, 0)
    for left in range(N):
        while right < N and tmp ^ A[right] == tmp + A[right]:
            tmp += A[right]
            ans += right - left + 1
            right += 1
        if left == right:
            right += 1
        else:
            tmp -= A[left]
    print(ans)


def __starting_point():
    main()


__starting_point()

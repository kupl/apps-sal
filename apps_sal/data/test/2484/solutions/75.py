import sys
import numpy as np

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))

    # a ^ b <= a + b が成り立つ
    ans = 0
    right = 0
    xor = 0
    s = 0
    for left in range(N):
        while right < N and s + A[right] == xor ^ A[right]:
            s += A[right]
            xor ^= A[right]
            right += 1

        ans += right - left

        if right == left:
            right += 1
        else:
            s -= A[left]
            xor ^= A[left]

    print(ans)


def __starting_point():
    main()

__starting_point()

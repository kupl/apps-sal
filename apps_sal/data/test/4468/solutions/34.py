from typing import List


def answer(N: int, T: int, t: List[int]) -> int:
    ans = 0
    for i in range(N - 1):
        ans += min(T, t[i + 1] - t[i])
    return ans + T


def main():
    N, T = list(map(int, input().split()))
    t = list(map(int, input().split()))
    print((answer(N, T, t)))


def __starting_point():
    main()


__starting_point()

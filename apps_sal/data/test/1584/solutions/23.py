
import bisect


def main():
    N = int(input())
    L = list(sorted(map(int, input().split())))
    res = 0
    for i in range(N - 2):
        x = L[i]
        for j in range(i + 1, N - 1):
            y = L[j]
            res += bisect.bisect_left(L, x + y) - j - 1

    print(res)
    return


main()

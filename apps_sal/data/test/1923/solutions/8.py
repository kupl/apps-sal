import sys
input = sys.stdin.readline


def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = sum((L[i] for i in range(0, 2 * N, 2)))
    print(ans)


def __starting_point():
    main()


__starting_point()

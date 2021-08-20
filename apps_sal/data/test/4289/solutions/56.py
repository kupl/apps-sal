import sys
input = sys.stdin.readline


def main():
    N = int(input())
    (T, A) = [int(x) for x in input().split()]
    H = [int(x) for x in input().split()]
    ans = 0
    sa = float('inf')
    for i in range(N):
        tmp = sa
        sa = min(sa, abs(T - H[i] * 0.006 - A))
        if sa != tmp:
            ans = i + 1
    print(ans)


def __starting_point():
    main()


__starting_point()

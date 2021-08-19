import sys
input = sys.stdin.readline


def main():
    (N, x) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - 1):
        if A[i] + A[i + 1] <= x:
            continue
        if A[i] >= x:
            ans += A[i] - x + A[i + 1]
            A[i] = x
            A[i + 1] = 0
        else:
            ans += A[i] + A[i + 1] - x
            A[i + 1] = x - A[i]
    print(ans)


def __starting_point():
    main()


__starting_point()

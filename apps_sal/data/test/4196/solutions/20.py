import sys
input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    left = [A[0]] * (N + 2)
    right = [A[-1]] * (N + 2)

    for i in range(N):
        left[i + 1] = gcd(left[i], A[i])
        right[N - i] = gcd(right[N - i + 1], A[N - 1 - i])
    # print(left)
    # print(right)
    ans = max(left[-3], right[2])
    for i in range(1, N + 1):
        ans = max(ans, gcd(left[i - 1], right[i + 1]))
    print(ans)


def __starting_point():
    main()


__starting_point()

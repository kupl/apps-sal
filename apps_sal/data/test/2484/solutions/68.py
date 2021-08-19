import sys
input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    r = 0
    b = A[0]
    ans = 0
    for l in range(N):
        while r + 1 < N and A[r + 1] & b == 0:
            r += 1
            b |= A[r]
        ans += r - l + 1
        b = b ^ A[l]
    print(ans)


def __starting_point():
    main()


__starting_point()

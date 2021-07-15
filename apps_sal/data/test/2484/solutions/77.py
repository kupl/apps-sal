import sys
input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(x) for x in input().split()]

    r = 0
    b = 0
    ans = 0
    for l in range(N):
        while r < N and A[r] & b == 0:
            b |= A[r]
            r += 1
        ans += r - l
        b = b ^ A[l]

    print(ans)




def __starting_point():
    main()


__starting_point()

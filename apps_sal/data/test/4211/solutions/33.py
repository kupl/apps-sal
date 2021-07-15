# coding: utf-8


def main():
    N = int(input())
    ans = 0
    B = list(map(int, input().split()))
    ans += B[0] + B[-1]

    for i in range(1, N - 1):
        ans += min(B[i - 1], B[i])

    print(ans)

def __starting_point():
    main()

__starting_point()

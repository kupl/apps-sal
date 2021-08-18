inf = float('inf')


def main():
    N = int(input())
    A = [0] + list(map(int, input().split()))

    dp1 = [-inf] * (N + 1)
    dp2 = [-inf] * (N + 1)
    dp1[1] = 0
    dp2[1] = 0
    dp1[2] = A[1]
    dp2[2] = A[2]
    for i in range(3, N + 1):
        if i % 2 == 0:
            dp1[i] = dp1[i - 2] + A[i - 1]
            dp2[i] = max(dp2[i - 2] + A[i], dp1[i - 2] + A[i])
        else:
            dp1[i] = max(dp2[i - 1], dp1[i - 2] + A[i - 1])
            dp2[i] = max(dp2[i - 2] + A[i], dp1[i - 2] + A[i])

    if N % 2 == 0:
        ans = max([dp1[N], dp2[N]])
    else:
        ans = max(dp1[-2:] + dp2[-2:])

    print(ans)


def __starting_point():
    main()


__starting_point()

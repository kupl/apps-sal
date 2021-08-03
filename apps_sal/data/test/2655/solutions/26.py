def ans():
    from math import floor
    N = int(input())
    A = [0] + list(map(int, input().split()))
    A = sorted(A)

    sum_conf = 0
    for k in range(1, N):
        sum_conf += A[N - floor(k / 2)]

    print(sum_conf)


def __starting_point():
    ans()


__starting_point()

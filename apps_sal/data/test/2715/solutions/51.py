def main():
    K = int(input())
    N = 50

    a = [N - 1] * N
    q, r = divmod(K, N)
    for i in range(N):
        cnt_add = q + int(i < r)
        a[i] += N * cnt_add
        a[i] -= K - cnt_add

    print(N)
    print((*a))


def __starting_point():
    main()

__starting_point()

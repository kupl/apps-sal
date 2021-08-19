def main():
    N, K = list(map(int, input().split(' ')))
    # K < b <= N
    # a =  K, ..., b - 1  # if K = 0, exclude the a = K case
    #      b + K, ..., b + b - 1
    #      2 * b + K, ..., 2 * b + b - 1
    #      ...
    ans = 0
    for b in range(K + 1, N + 1):
        ans += (N // b) * (b - K)
        ans += max([0, N % b - K + 1])
        if K == 0:
            ans -= 1
    print(ans)


def __starting_point():
    main()


__starting_point()

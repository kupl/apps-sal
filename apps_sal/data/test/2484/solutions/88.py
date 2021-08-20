def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    ng = 0
    cum_xor = 0
    right = 0
    for left in range(N):
        if left > 0:
            cum_xor ^= A[left - 1]
        while right < N and cum_xor & A[right] == 0:
            cum_xor ^= A[right]
            right += 1
        ng += N - right
    print(N * (N + 1) // 2 - ng)


def __starting_point():
    main()


__starting_point()

def main():
    (N, X) = list(map(int, input().split()))
    nums = [None] * (N + 1)
    pnums = [None] * (N + 1)
    nums[0] = 1
    pnums[0] = 1
    for i in range(N):
        nums[i + 1] = nums[i] * 2 + 3
        pnums[i + 1] = pnums[i] * 2 + 1
    ans = 0
    while N >= 0:
        if N == 0:
            print(ans + 1)
            break
        if X == 1:
            print(ans)
            break
        elif X <= nums[N - 1] + 1:
            X -= 1
            N -= 1
        elif X == nums[N - 1] + 2:
            print(ans + pnums[N - 1] + 1)
            break
        elif X < nums[N]:
            X -= nums[N - 1] + 2
            ans += pnums[N - 1] + 1
            N -= 1
        else:
            print(ans + pnums[N])
            break


def __starting_point():
    main()


__starting_point()

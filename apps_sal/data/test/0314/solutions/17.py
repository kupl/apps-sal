def main():
    (N, K) = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    aran = 0
    bran = 0
    for n in range(N):
        aran += nums[n]
        x = min(aran, 8)
        aran -= x
        bran += x
        if bran >= K:
            print(n + 1)
            return
    print(-1)
    return


def __starting_point():
    main()


__starting_point()

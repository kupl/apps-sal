M, K = list(map(int, input().split()))

if K >= 2 ** M:
    print((-1))
elif (M, K) == (1, 0):
    print((*(0, 0, 1, 1)))
elif (M, K) == (1, 1):
    print((-1))
else:
    # 3, 5 -> [7 6 4 3 2 1 0 5 0 1 2 3 4 6 7 5]
    ans = [0] * (2 ** (M + 1))
    ans[2 ** M - 1] = ans[-1] = K

    num = 0
    for i in range(2 ** M - 1):
        if num == K:
            num += 1
        ans[2 ** M - i - 2] = ans[2 ** M + i] = num
        num += 1
    print((*ans))

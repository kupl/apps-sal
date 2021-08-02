def solve():
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    diff_0_1 = A[0] - A[1]
    A[1] += diff_0_1
    A[2] += diff_0_1
    cnt = diff_0_1

    diff_0_2 = A[0] - A[2]
    if diff_0_2 % 2 == 0:
        cnt += diff_0_2 // 2
    else:
        cnt += diff_0_2 // 2 + 1 + 1

    print(cnt)


def __starting_point():
    solve()


__starting_point()

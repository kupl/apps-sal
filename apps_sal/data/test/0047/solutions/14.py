def solve():
    N, X = map(int, input().split())
    A = [int(k) for k in input().split()]

    ans = 0
    cur_max1 = 0
    cur_max2 = 0
    cur_max3 = 0

    for a in A:
        '''
        if A[i] > cur_max + A[i]:
            cur_max = A[i]
        else:
            cur_max += A[i]'''

        cur_max1 = max(a, cur_max1 + a)
        cur_max2 = max(a * X, a * X + cur_max2, cur_max1)
        cur_max3 = max(a, cur_max3 + a, cur_max2)

        ans = max(ans, cur_max1, cur_max2, cur_max3, 0)

    print(ans)


def __starting_point():
    solve()


__starting_point()

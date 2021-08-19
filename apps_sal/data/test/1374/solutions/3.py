
def median_of_medians(N: int, A: list) -> int:
    def search(c):
        bar = N
        r = 0
        res_nega = 0
        dp_arr = [0] * (2 * N + 1)
        for i in range(N):
            dp_arr[bar] += 1
            if A[i] < c:
                r += dp_arr[bar]
                bar += 1
            else:
                r -= (dp_arr[bar - 1])
                bar -= 1
            res_nega += r
        return res_nega

    # binary search
    a_sorted = sorted(A)
    left = 0
    right = N
    mid = N // 2
    C = N * (N + 1) // 2
    while True:
        if search(a_sorted[mid]) <= C // 2:
            if mid == N - 1:
                break
            elif search(a_sorted[mid + 1]) > C // 2:
                break
            else:
                left = mid
                mid = (mid + right) // 2
        else:
            right = mid + 1
            mid = (mid + left) // 2

    return a_sorted[mid]


def __starting_point():
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = median_of_medians(N, A)
    print(ans)


__starting_point()

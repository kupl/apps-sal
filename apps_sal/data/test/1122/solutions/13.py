def main():
    n, m = list(map(int, input().split()))
    left = 1
    right = n
    is_shift = False
    ans = []
    while left < right:
        if right - left <= n // 2 and not is_shift and n % 2 == 0:
            left += 1
            is_shift = True
        ans.append([left, right])
        left += 1
        right -= 1

    for l in range(m):
        print((*ans[l]))


def __starting_point():
    main()


__starting_point()

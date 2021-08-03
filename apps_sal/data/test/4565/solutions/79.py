def main():
    n = int(input())
    ss = list(input())
    num_sum = [0] * n
    west_sum = 0
    east_sum = 0
    for i in range(1, n):
        if ss[i - 1] == 'W':
            west_sum += 1
        num_sum[i] += west_sum

    for i in range(n - 2, -1, -1):
        if ss[i + 1] == 'E':
            east_sum += 1
        num_sum[i] += east_sum

    ans = min(num_sum)
    print(ans)


def __starting_point():
    main()


__starting_point()

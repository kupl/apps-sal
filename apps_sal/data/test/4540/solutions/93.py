def main():
    n = int(input())
    As = [0] + list(map(int, input().split())) + [0]

    cumsum = [0] * (n + 1)
    for i in range(1, n + 2):
        cumsum[i - 1] = abs(As[i] - As[i - 1])
    cumsum_sum = sum(cumsum)
    for i in range(1, n + 1):
        ans = cumsum_sum - cumsum[i - 1] - cumsum[i] + abs(As[i + 1] - As[i - 1])
        print(ans)


def __starting_point():
    main()


__starting_point()

from bisect import bisect_right


def make_divisers(n):
    upper_result = []
    lower_result = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            lower_result.append(i)
            ii = n // i
            if ii != i:
                upper_result.append(ii)
    return lower_result + upper_result[::-1]


def main():
    (N, M) = map(int, input().split())
    divisers = make_divisers(M)
    idx = bisect_right(divisers, M / N) - 1
    print(divisers[idx])


def __starting_point():
    main()


__starting_point()

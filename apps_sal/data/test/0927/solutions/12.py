def num_to_match(n):
    if n == 1:
        return 2
    elif n == 7:
        return 3
    elif n == 4:
        return 4
    elif n in [2, 3, 5]:
        return 5
    elif n in [6, 9]:
        return 6
    else:
        return 7


def max_length(N, match):
    match = set(match)
    INF = 10 ** 15
    dp = [-INF for _ in range(N + 1)]
    dp[0] = 0
    for n in range(1, N + 1):
        max_l = dp[n]
        for m in match:
            if n - m >= 0 and dp[n - m] >= 0:
                max_l = max([max_l, 1 + dp[n - m]])
        dp[n] = max_l
    return dp


def main():
    (N, _) = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    A.sort(reverse=True)
    match = list(map(num_to_match, A))
    max_l = max_length(N, match)
    digits = [0 for _ in range(max_l[N])]
    n_match = N
    for i in range(max_l[N]):
        for a in A:
            ma = num_to_match(a)
            if n_match - ma < 0:
                continue
            if max_l[n_match - ma] == max_l[n_match] - 1:
                digits[i] = a
                n_match -= ma
                break
    print(''.join(map(str, digits)))


def __starting_point():
    main()


__starting_point()

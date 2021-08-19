def f(n, a_list):
    a_list = list(zip(list(range(n)), a_list))
    a_list.sort(key=lambda x: x[1])
    dp = [0]
    for k in range(1, n + 1):
        dp_ = []
        (i, a) = a_list.pop()
        dp_.append(dp[0] + a * (n - k - i))
        for x in range(1, k):
            dp_.append(max(dp[x - 1] + a * (i - x + 1), dp[x] + a * (n - k + x - i)))
        dp_.append(dp[k - 1] + a * (i - k + 1))
        dp = dp_
    return max(dp)


def __starting_point():
    n = int(input())
    a_list = list(map(int, input().split()))
    print(f(n, a_list))


__starting_point()

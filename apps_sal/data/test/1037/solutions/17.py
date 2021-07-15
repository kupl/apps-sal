def f(n, a_list):
    a_list = list(zip(list(range(n)), a_list))
    a_list.sort(key=lambda x: x[1])
    # a_list[j][0]: (j + 1)番目に小さい活発度をもつ幼児の座標
    # a_list[j][1]: ↑の活発度
    dp = [0]
    # dp[x]: x 人を左, (k - x) 人を右に置く場合
    for k in range(1, n + 1):
        dp_ = []
        i, a = a_list.pop()  # i: 座標, a: 活発度
        dp_.append(dp[0] + a * (n - k - i))
        for x in range(1, k):
            dp_.append(max(dp[x - 1] + a * (i - x + 1),
                           dp[x] + a * (n - k + x - i)))
        dp_.append(dp[k - 1] + a * (i - k + 1))
        dp = dp_
    return max(dp)


def __starting_point():
    n = int(input())
    a_list = list(map(int, input().split()))
    print((f(n, a_list)))

__starting_point()

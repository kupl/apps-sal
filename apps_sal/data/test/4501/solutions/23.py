def c_tak_and_cards():
    from collections import defaultdict
    N, A = [int(i) for i in input().split()]
    X = [int(i) for i in input().split()]

    average = [x - A for x in X]
    dp = defaultdict(int)  # dp[s]: y から 1 枚以上選んで整数の和を s にする方法
    dp[0] = 1  # 「選ばない」 1 通り
    for y in average:
        for k, v in list(dp.items()):  # for 文中で要素数が変わってはいけないため
            dp[k + y] += v
    return dp[0] - 1


print(c_tak_and_cards())

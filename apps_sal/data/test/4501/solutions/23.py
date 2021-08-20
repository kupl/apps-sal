def c_tak_and_cards():
    from collections import defaultdict
    (N, A) = [int(i) for i in input().split()]
    X = [int(i) for i in input().split()]
    average = [x - A for x in X]
    dp = defaultdict(int)
    dp[0] = 1
    for y in average:
        for (k, v) in list(dp.items()):
            dp[k + y] += v
    return dp[0] - 1


print(c_tak_and_cards())

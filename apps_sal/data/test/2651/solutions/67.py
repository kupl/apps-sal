def d_rectangles(MOD=10**9 + 7):
    N, M = [int(i) for i in input().split()]
    X = [int(i) for i in input().split()]
    Y = [int(i) for i in input().split()]

    ans1 = sum([x * (2 * k - N - 1) for k, x in enumerate(X, 1)])
    ans2 = sum([y * (2 * k - M - 1) for k, y in enumerate(Y, 1)])
    return (ans1 * ans2) % MOD


print(d_rectangles())

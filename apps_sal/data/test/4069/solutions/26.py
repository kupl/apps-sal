def main(X, K, D):
    ans = 0
    X = abs(X)
    time = round(X // D)
    if time > K:
        time = K
    if time == 0:
        if X <= abs(X - D):
            time = 0
        else:
            time = 1
    ans = X - time * D
    if (K - time) % 2 != 0:
        ans = abs(ans) - D
    return abs(ans)


def __starting_point():
    X, K, D = list(map(int, input().split()))
    ans = main(X, K, D)
    print(ans)


__starting_point()

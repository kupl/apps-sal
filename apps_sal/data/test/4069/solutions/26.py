def main(X, K, D):
    ans = 0
    X = abs(X)
    # 0に近づける回数を獲得
    time = round(X // D)
    #print(f'time: {time}')
    if time > K:
        time = K
    #print(f'time: {time}')
    if time == 0:
        # Xとabs(X-D)のどちらがより0に近いのか
        if X <= abs(X - D):
            time = 0
        else:
            time = 1
    #print(f'time: {time}')
    # それ以外の回数は単に往復する
    ans = X - time * D
    if (K - time) % 2 != 0:
        ans = abs(ans) - D
    return abs(ans)


def __starting_point():
    X, K, D = list(map(int, input().split()))
    ans = main(X, K, D)
    print(ans)


__starting_point()

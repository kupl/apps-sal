
def resolve():
    N, X = map(int, input().split())

    As = [1]  # レベルiバーガーの厚さ（層の総数）（必ず奇数）
    Ps = [1]  # レベルiバーガーのパティの総数

    for i in range(N):
        As.append(As[i] * 2 + 3)  # レベルが1上がると、総数は2倍+3になる
        Ps.append(Ps[i] * 2 + 1)  # レベルが1上がると、パティの数は2倍+1になる

    def f(n, x):
        if n == 0:
            return 0 if x <= 0 else 1
        mid = (As[n] + 1) // 2

        # バーガーの真ん中にはパティがある。そのパティを含むかの場合分けをする
        if x < mid:
            return f(n - 1, x - 1)
        elif x == mid:
            return Ps[n - 1] + 1
        elif x > mid:
            return Ps[n - 1] + 1 + f(n - 1, x - mid)

    ans = f(N, X)

    print(ans)


def __starting_point():
    resolve()


__starting_point()

def main():
    from collections import namedtuple
    import sys
    input = sys.stdin.readline

    Sushi = namedtuple('Sushi', 'x cal')

    n, c = list(map(int, input().split()))

    a = []
    for _ in range(n):
        x, v = list(map(int, input().split()))
        a.append(Sushi(x=x, cal=v))
    # x昇順ソート済

    clock = [0] * (n + 1)  # 注目する寿司以前で離脱する最大摂取カロリー
    clock_to_0 = [0] * (n + 1)  # 時計回り->初期位置の最大摂取カロリー
    ma = 0  # 注目する寿司以前で離脱する最大摂取カロリー
    ma0 = 0  # 時計回り->初期位置の最大摂取カロリー
    curr = 0  # 現在のカロリー(移動によるカロリー消費を無視)
    for i, s in enumerate(a, start=1):
        curr += s.cal
        ma = max(ma, curr - s.x)
        ma0 = max(ma0, curr - s.x * 2)
        clock[i] = ma
        clock_to_0[i] = ma0

    anti = [0] * (n + 1)  # 注目する寿司以前で離脱する最大摂取カロリー
    anti_to_0 = [0] * (n + 1)  # 反時計回り->初期位置の最大摂取カロリー
    ma = 0  # 注目する寿司以前で離脱する最大摂取カロリー
    ma0 = 0  # 時計回り->初期位置の最大摂取カロリー
    curr = 0  # 現在のカロリー(移動によるカロリー消費を無視)
    for i, s in zip(list(range(n, -1, -1)), reversed(a)):
        curr += s.cal
        ma = max(ma, curr - (c - s.x))
        ma0 = max(ma0, curr - (c - s.x) * 2)
        anti[i] = ma
        anti_to_0[i] = ma0

    ans = 0
    for exit_pos in range(1, n + 1):
        ans = max(
            ans,
            clock_to_0[exit_pos - 1] + anti[exit_pos],
            anti_to_0[(exit_pos + 1) % (n + 1)] + clock[exit_pos]
        )

    print(ans)


def __starting_point():
    main()


__starting_point()

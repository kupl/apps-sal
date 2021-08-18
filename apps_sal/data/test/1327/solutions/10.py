import sys


def get_input() -> tuple:
    """
    標準入力を取得.

    Returns:\n
        tuple: 標準入力
    """
    N, M = list(map(int, input().split()))
    cakes = []
    for n in range(N):
        cake_n = list(map(int, input().split()))
        cakes.append(cake_n)

    return N, M, cakes


def main(N: int, M: int, cakes: list) -> None:
    """
    メイン処理.

    Args:\n
        N (int): ケーキの種類(1 <= N <= 1000)
        M (int): 食べる数(0 <= M <= N)
        cakes (list): ケーキの要素(-10000000000 <= x_i, y_i, z_i <= 10000000000)
    """
    ans = -sys.maxsize
    element = 3
    for bit in range(1 << element):
        sign = [1 for i in range(element)]
        for i in range(element):
            if bit & (1 << i):
                sign[i] *= -1
        cakes = sorted(cakes, key=lambda x: sum(
            [sign[i] * x[i] for i in range(element)]), reverse=True)

        indicator = [0 for i in range(element)]
        for cake in cakes[:M]:
            for i in range(element):
                indicator[i] += cake[i]

        ans = max(ans, sum(map(abs, indicator)))

    print(ans)


def __starting_point():
    N, M, cakes = get_input()

    main(N, M, cakes)


__starting_point()

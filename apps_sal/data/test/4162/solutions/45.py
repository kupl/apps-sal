# -*- coding: utf-8 -*-

def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    N = int(input())
    a = list(map(int, input().split()))

    return N, a


def main(N: int, a: list) -> None:
    """
    メイン処理.

    Args:\n
        N (int): 正整数の数(2 <= N <= 3000)
        a (list): 正整数(2 <= a_i <= 10^5)
    """
    # 求解処理
    ans = sum(a) - N

    # 結果出力
    print(ans)


def __starting_point():
    # 標準入力を取得
    N, a = get_input()

    # メイン処理
    main(N, a)


__starting_point()

# -*- coding: utf-8 -*-

def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    # 標準入力を取得
    D, N = list(map(int, input().split()))

    return D, N


def main(D: int, N: int) -> None:
    """
    メイン処理.

    Args:\n
        D (int): 0, 1, or 2
        N (int): 整数(1 <= N <= 100)
    """
    # 求解処理
    ans = (N + (N // 100)) * 100**D

    # 結果出力
    print(ans)


def __starting_point():
    # 標準入力を取得
    D, N = get_input()

    # メイン処理
    main(D, N)


__starting_point()

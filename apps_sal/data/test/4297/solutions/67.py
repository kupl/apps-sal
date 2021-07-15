# -*- coding: utf-8 -*-

def get_input() -> int:
    """
    標準入力を取得する.

    Returns:\n
        int: 標準入力
    """
    N = int(input())

    return N


def main(N: int) -> None:
    """
    メイン処理.

    Args:\n
        N (int): 正整数(1 <= N <= 10^9)
    """
    # 求解処理
    ans = N
    if ans % 2 != 0:
        ans *= 2

    # 結果出力
    print(ans)


def __starting_point():
    # 標準入力を取得
    N = get_input()

    # メイン処理
    main(N)

__starting_point()

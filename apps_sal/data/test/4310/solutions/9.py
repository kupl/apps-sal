# -*- coding: utf-8 -*-

def get_input() -> list:
    """
    標準入力を取得する.

    Returns:\n
        list: 標準入力
    """
    A = list(map(int, input().split()))

    return A


def main(A: list) -> None:
    """
    メイン処理.

    Args:\n
        A (list): 整数列(1 <= A_i <= 100)
    """
    # 求解処理
    ans = max(A) - min(A)

    # 結果出力
    print(ans)


def __starting_point():
    # 標準入力を取得
    A = get_input()

    # メイン処理
    main(A)

__starting_point()

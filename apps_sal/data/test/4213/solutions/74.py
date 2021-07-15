# -*- coding: utf-8 -*-

def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    N = int(input())
    A = list(map(int, input().split()))

    return N, A


def main(A: list) -> None:
    """
    メイン処理.

    Args:\n
        A (list): 整数列(1 <= A_i <= 10^9)
    """
    # 求解処理
    ans = max(A) - min(A)

    # 結果出力
    print(ans)


def __starting_point():
    # 標準入力を取得
    N, A = get_input()

    # メイン処理
    main(A)

__starting_point()

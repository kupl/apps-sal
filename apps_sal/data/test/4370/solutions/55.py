# -*- coding: utf-8 -*-

def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    A, B = list(map(int, input().split()))

    return A, B


def main(A: int, B: int) -> None:
    """
    メイン処理.

    Args:\n
        A (int): 切れ(1 <= A <= 16)
        B (int): 切れ(1 <= B <= 16)
    """
    # 求解処理
    ans = str()
    if (A <= 8) and (B <= 8):
        ans = "Yay!"
    else:
        ans = ":("

    # 結果出力
    print(ans)


def __starting_point():
    # 標準入力を取得
    A, B = get_input()

    # メイン処理
    main(A, B)


__starting_point()

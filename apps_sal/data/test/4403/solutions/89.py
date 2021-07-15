# -*- coding: utf-8 -*-

def get_input() -> str:
    """
    標準入力を取得する.

    Returns:\n
        str: 標準入力
    """
    S = input()

    return S


def main(S: str) -> None:
    """
    メイン処理.

    Args:\n
        S (str): 文字列(|S| = 4, 各文字は"+"または"-")
    """
    # 求解処理
    ans = S.count("+") - S.count("-")

    # 結果出力
    print(ans)


def __starting_point():
    # 標準入力を取得
    S = get_input()

    # メイン処理
    main(S)

__starting_point()

# -*- coding: utf-8 -*-

def get_input() -> int:
    """
    標準入力を取得する.

    Returns:\n
        int: 標準入力
    """
    N = int(input())

    return N


def S(n: int) -> int:
    """
    各桁の和を取得する.

    Args:\n
        n (int): 整数

    Returns:\n
        int: 各桁の和
    """
    return sum(map(int, str(n)))


def main(N: int) -> None:
    """
    メイン処理.

    Args:\n
        N (int): 整数(1 <= N <= 10**9)
    """
    # 求解処理
    ans = str()
    if N % S(N) == 0:
        ans = "Yes"
    else:
        ans = "No"

    # 結果出力
    print(ans)


def __starting_point():
    # 標準入力を取得
    N = get_input()

    # メイン処理
    main(N)

__starting_point()

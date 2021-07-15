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


def get_divisible_count(x: int) -> int:
    """
    2で何回割ることができるかを返す.

    Args:\n
        x (int): 整数

    Returns:\n
        int: 2で割ることができる回数
    """
    divisible_count = 0
    while x % 2 == 0:
        divisible_count += 1
        x /= 2
    return divisible_count


def main(N: int, a: list) -> tuple:
    """
    メイン処理.

    Args:\n
        N (int): 数列の長さ(1 <= N <= 10000)
        a (list): 数列(1 <= a_i <= 1000000000)

    Returns:\n
        tuple: [description]
    """
    ans = 0
    for n in range(N):
        ans += get_divisible_count(a[n])

    # 結果出力
    print(ans)


def __starting_point():
    # 標準入力を取得
    N, a = get_input()

    # メイン処理
    main(N, a)

__starting_point()

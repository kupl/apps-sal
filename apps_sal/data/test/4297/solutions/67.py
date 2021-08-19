def get_input() -> int:
    """
    標準入力を取得する.

    Returns:

        int: 標準入力
    """
    N = int(input())
    return N


def main(N: int) -> None:
    """
    メイン処理.

    Args:

        N (int): 正整数(1 <= N <= 10^9)
    """
    ans = N
    if ans % 2 != 0:
        ans *= 2
    print(ans)


def __starting_point():
    N = get_input()
    main(N)


__starting_point()

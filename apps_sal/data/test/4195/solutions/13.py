def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:

        tuple: 標準入力
    """
    (D, N) = list(map(int, input().split()))
    return (D, N)


def main(D: int, N: int) -> None:
    """
    メイン処理.

    Args:

        D (int): 0, 1, or 2
        N (int): 整数(1 <= N <= 100)
    """
    ans = (N + N // 100) * 100 ** D
    print(ans)


def __starting_point():
    (D, N) = get_input()
    main(D, N)


__starting_point()

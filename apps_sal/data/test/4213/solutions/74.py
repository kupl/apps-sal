def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:

        tuple: 標準入力
    """
    N = int(input())
    A = list(map(int, input().split()))
    return (N, A)


def main(A: list) -> None:
    """
    メイン処理.

    Args:

        A (list): 整数列(1 <= A_i <= 10^9)
    """
    ans = max(A) - min(A)
    print(ans)


def __starting_point():
    (N, A) = get_input()
    main(A)


__starting_point()

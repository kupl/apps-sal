
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
    ans = max(A) - min(A)

    print(ans)


def __starting_point():
    A = get_input()

    main(A)


__starting_point()

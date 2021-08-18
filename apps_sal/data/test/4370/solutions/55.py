
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
    ans = str()
    if (A <= 8) and (B <= 8):
        ans = "Yay!"
    else:
        ans = ":("

    print(ans)


def __starting_point():
    A, B = get_input()

    main(A, B)


__starting_point()

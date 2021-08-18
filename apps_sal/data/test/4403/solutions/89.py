
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
    ans = S.count("+") - S.count("-")

    print(ans)


def __starting_point():
    S = get_input()

    main(S)


__starting_point()

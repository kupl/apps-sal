def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:

        tuple: 標準入力
    """
    S = input()
    T = input()
    return (S, T)


def main(S: str, T: str) -> None:
    """
    メイン処理.

    Args:

        S (str): 英子文字からなる文字列(2 <= |S| <= 100)
        T (str): 英子文字からなる文字列(|S| = |T|)
    """
    N = len(S)
    ans = 'No'
    for i in range(N):
        if S[-i:] + S[:-i] == T:
            ans = 'Yes'
            break
    print(ans)


def __starting_point():
    (S, T) = get_input()
    main(S, T)


__starting_point()

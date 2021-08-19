def get_input() -> int:
    """
    標準入力を取得する.

    Returns:

        int: 標準入力
    """
    N = int(input())
    return N


def S(n: int) -> int:
    """
    各桁の和を取得する.

    Args:

        n (int): 整数

    Returns:

        int: 各桁の和
    """
    return sum(map(int, str(n)))


def main(N: int) -> None:
    """
    メイン処理.

    Args:

        N (int): 整数(1 <= N <= 10**9)
    """
    ans = str()
    if N % S(N) == 0:
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)


def __starting_point():
    N = get_input()
    main(N)


__starting_point()

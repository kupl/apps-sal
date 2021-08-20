def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:

        tuple: 標準入力
    """
    (N, K) = list(map(int, input().split()))
    return (N, K)


def main(N: int, K: int) -> None:
    """
    メイン処理.

    Args:

        N (int): せんべいの枚数(1 <= N <= 100)
        K (int): 参加人数(1 <= K <= 100)
    """
    ans = 0
    if N % K != 0:
        ans = 1
    print(ans)


def __starting_point():
    (N, K) = get_input()
    main(N, K)


__starting_point()

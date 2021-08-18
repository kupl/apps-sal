import itertools


def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    N = int(input())
    A = list(map(int, input().split()))

    return N, A


def main(A: list) -> None:
    """
    メイン処理.

    Args:\n
        A (list): 整数列(1 <= A_i <= 10^9)
    """
    ans = 0
    for A_i, A_j in itertools.combinations(A, r=2):
        ans = max(ans, abs(A_i - A_j))

    print(ans)


def __starting_point():
    N, A = get_input()

    main(A)


__starting_point()

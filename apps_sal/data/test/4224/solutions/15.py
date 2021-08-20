def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:

        tuple: 標準入力
    """
    N = int(input())
    a = list(map(int, input().split()))
    return (N, a)


def get_divisible_count(x: int) -> int:
    """
    2で何回割ることができるかを返す.

    Args:

        x (int): 整数

    Returns:

        int: 2で割ることができる回数
    """
    divisible_count = 0
    while x % 2 == 0:
        divisible_count += 1
        x /= 2
    return divisible_count


def main(N: int, a: list) -> tuple:
    """
    メイン処理.

    Args:

        N (int): 数列の長さ(1 <= N <= 10000)
        a (list): 数列(1 <= a_i <= 1000000000)

    Returns:

        tuple: [description]
    """
    ans = 0
    for n in range(N):
        ans += get_divisible_count(a[n])
    print(ans)


def __starting_point():
    (N, a) = get_input()
    main(N, a)


__starting_point()

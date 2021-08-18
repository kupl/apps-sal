
def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    return N, A, B, C


def get_lb(l: list, key: int) -> int:
    """
    l[index] > keyとなる最小のindexを求める.

    Args:\n
        l (list): リスト
        key (int): 整数

    Returns:\n
        int: l[index] > keyとなる最小のindex
    """
    low = -1
    high = len(l)
    while 1 < high - low:
        mid = (low + high) // 2
        guess = l[mid]
        if guess > key:
            high = mid
        else:
            low = mid
    return high


def get_ub(l: list, key: int) -> int:
    """
    l[index] < keyとなる最大のindexを求める.

    Args:\n
        l (list): リスト
        key (int): 整数

    Returns:\n
        int: l[index] < keyとなる最大のindex
    """
    low = -1
    high = len(l)
    while 1 < high - low:
        mid = (low + high) // 2
        guess = l[mid]
        if guess < key:
            low = mid
        else:
            high = mid
    return low


def main(N: int, A: list, B: list, C: list) -> None:
    """
    メイン処理.

    Args:\n
        N (int): パーツの数(1 <= N <= 10**5)
        A (list): 上部のパーツのサイズ(1 <= A_i <= 10**9)
        B (list): 中部のパーツのサイズ(1 <= B_i <= 10**9)
        C (list): 下部のパーツのサイズ(1 <= C_i <= 10**9)
    """
    A = sorted(A)
    B = sorted(B)
    C = sorted(C)

    ans = 0
    for i in range(N):
        B_i = B[i]
        ans += (get_ub(A, B_i) + 1) * (N - get_lb(C, B_i))

    print(ans)


def __starting_point():
    N, A, B, C = get_input()

    main(N, A, B, C)


__starting_point()

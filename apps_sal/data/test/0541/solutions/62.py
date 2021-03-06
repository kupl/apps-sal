def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:

        tuple: 標準入力
    """
    (N, M) = list(map(int, input().split()))
    requests = []
    for i in range(M):
        (a_i, b_i) = list(map(int, input().split()))
        requests.append((a_i, b_i))
    return (N, M, requests)


def main(N: int, M: int, requests: list) -> None:
    """
    メイン処理.

    Args:

        N (int): 島の数(2 <= N <= 10^5)
        M (int): 要望の数(1 <= M <= 10^5)
        requests (list): 要望(1 <= a_i < b_i <= N)
    """
    requests = sorted(requests, key=lambda x: x[1])
    bridge = 0
    ans = 0
    for i in range(M):
        (a_i, b_i) = requests[i]
        if a_i > bridge:
            bridge = b_i - 1
            ans += 1
    print(ans)


def __starting_point():
    (N, M, requests) = get_input()
    main(N, M, requests)


__starting_point()

import math


def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:

        tuple: 標準入力
    """
    (D, G) = list(map(int, input().split()))
    (p, c) = ([], [])
    for i in range(D):
        (p_i, c_i) = list(map(int, input().split()))
        p.append(p_i)
        c.append(c_i)
    return (D, G, p, c)


def main(D: int, G: int, p: list, c: list) -> None:
    """
    メイン処理.

    Args:

        D (int): 難易度の数(1 <= D <= 10)
        G (int): 目標スコア(100 <= G, 100の倍数)
        p (list): 問題数(1 <= p_i <= 100)
        c (list): コンプリートボーナス(100 <= c_i <= 10^6, 100の倍数)
    """
    ans = sum(p)
    for bit in range(2 << D):
        d = 0
        cnt = 0
        score = 0
        for i in range(D):
            if bit >> i & 1:
                cnt += p[i]
                score += 100 * (i + 1) * p[i] + c[i]
            else:
                d = i
        if score < G:
            cnt_d = min(math.ceil((G - score) / (100 * (d + 1))), p[d] - 1)
            cnt += cnt_d
            score += 100 * (d + 1) * cnt_d
        if score >= G:
            ans = min(ans, cnt)
    print(ans)


def __starting_point():
    (D, G, p, c) = get_input()
    main(D, G, p, c)


__starting_point()

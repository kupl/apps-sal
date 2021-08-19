import sys
from collections import defaultdict

mod = 10 ** 9 + 7


def factorization(n):
    """ n の素因数分解

    Args:
        n (int): [description]

    Returns:
        [type]: [description]
    """

    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):  # sqrt(n) まで
        # i で割れるだけ割る、を繰り返す
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])  # 結果を追加

    if tmp != 1:
        arr.append([tmp, 1])  # まだ余っていれば追加しておく

    if arr == []:
        arr.append([n, 1])  # このブロック、必要か？

    return arr


def main():

    N = int(sys.stdin.readline().rstrip())
    A = [int(x) for x in sys.stdin.readline().rstrip().split()]

    # 最小公倍数を作る
    p = defaultdict(int)  # p に 因数 : 指数 でもたせる
    for a in A:
        for x, y in factorization(a):
            p[x] = max(p[x], y)

    # 一旦、全部の掛け合わせを作る
    U = 1
    for x, y in p.items():
        U = (U * pow(x, y, mod)) % mod

    # 足す
    ans = 0
    for a in A:
        ans = (ans + U * pow(a, mod - 2, mod)) % mod  # 逆元を

    print(ans)


main()

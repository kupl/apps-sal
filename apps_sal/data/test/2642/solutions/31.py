from bisect import bisect_left, bisect_right
from fractions import Fraction
from collections import defaultdict
import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    # a!=0 かつ b!=0
    AB = []
    # a!=0 または b!=0
    ZAB = []
    M = 0
    ZM = 0
    for i in range(N):
        a, b = map(int, input().strip().split())
        # (a, b) == (0, 0) は除外する
        if a != 0 or b != 0:
            AB.append((a, b))
            M += 1
    return N, M, AB


def solve(N, M, AB, MOD=1000000007):
    # 魚iに対して、仲の悪い魚jの個数を求める
    D = defaultdict(int)
    INVD = defaultdict(int)

    # Ai/Bi の既約分数でグループを作る
    keys = set()
    for a, b in AB:
        if a == 0:
            # 0/Bi
            D["0"] += 1
            keys.add("0")
        elif b == 0:
            # Ai/0
            INVD["0"] += 1
            keys.add("0")
        else:
            f = Fraction(a, b)
            if f > 0:
                key = str(f)
                D[key] += 1
                keys.add(key)
            else:
                key = str(-1 / f)
                INVD[key] += 1
                keys.add(key)

    # a!=0 かつ b!=0 における魚群の選び方を数え上げ
    # グループiにおいて
    # (1-1) D[i] 個の魚から1つ以上選ぶ ... (2^D[i] - 1) 通り
    # (1-2) INVD[i] 個の魚から1つ以上選ぶ ... (2^INVD[i] - 1) 通り
    # (1-3) グループi から魚を選ばない ... 1通り
    ans = 1
    for key in keys:
        g1 = pow(2, D[key], MOD) - 1
        g2 = pow(2, INVD[key], MOD) - 1
        g3 = 1
        ans *= (g1 + g2 + g3)
        ans %= MOD

    # 魚を1つも選ばない場合が含まれているので、これを除く
    ans -= 1
    ans %= MOD

    # (a, b) == (0, 0) があるときは、その1匹だけなら入れられる
    ans += N - M
    ans %= MOD

    return ans


def __starting_point():
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))


__starting_point()

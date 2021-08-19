
from fractions import Fraction
from collections import defaultdict


def resolve():
    # A1*A2 + B1*B2 = 0 式変形 A1/B1 = -(B2/A2)
    # a, b の0がある条件を考える

    MOD = 1000000007
    N = int(input())
    zeroes = 0
    hash1 = defaultdict(int)
    hash2 = defaultdict(str)  # 中の悪い相手を記入
    for _ in range(N):
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            zeroes += 1
        elif b == 0:
            hash1["1/0"] += 1
            hash2["1/0"] = "0/1"
        elif a == 0:
            hash1["0/1"] += 1
            hash2["0/1"] = "1/0"
        else:  # a, bが0以外
            rat1 = Fraction(a, b)
            rat2 = Fraction(-b, a)
            hash1[str(rat1)] += 1
            hash2[str(rat1)] = str(rat2)  # 相手を入れる

    confirmed = set()
    ans = 1
    for k, v in hash1.items():
        if k in confirmed:  # 確認済みを数えないようにする
            continue
        bad = hash1.get(hash2[k], 0)  # 中の悪い相手, キーがなかったら0を出力
        cnt1 = pow(2, v, MOD) - 1
        cnt2 = pow(2, bad, MOD) - 1
        ans = (ans * (cnt1 + cnt2 + 1)) % MOD
        # 確認済みにする
        confirmed.add(k)
        confirmed.add(hash2[k])
        # ※ ループ中に値を変更したらエラー
        # hash1[k] = -1

    ans = (ans + zeroes + MOD - 1) % MOD
    print(ans)


def __starting_point():
    resolve()


__starting_point()

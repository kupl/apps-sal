# 2回前までのを保存しておく全探索？
# -> ATGC ACGC AGGC の場合も条件を満たしてしまうので、3つ前までかも（気づくのに長時間かかった）
# -> AGxCの場合も気づかなかった...

# なぜかサンプル3が合わないがコードが間違ってるわけないので表記ミスと判断して提出（傲慢
# -> MODしてないだけだった...

n = int(input())
if n == 3:
    print((61))
    return

memo = {}
MOD = 10**9 + 7


def rec(i, pre3, pre2, pre1):
    if pre3 == "A" and pre2 == "G" and pre1 == "C":
        return 0
    if pre3 == "G" and pre2 == "A" and pre1 == "C":
        return 0
    if pre3 == "A" and pre2 == "C" and pre1 == "G":
        return 0
    if (i, pre1, pre2, pre3) in memo:
        return memo[(i, pre1, pre2, pre3)]
    if i == n - 3:
        return 1
    else:
        ret = 0
        if (pre1 == "G" and pre2 == "A") or (pre1 == "A" and pre2 == "G"):
            ret = rec(i + 1, pre2, pre1, "A") % MOD + rec(
                i + 1, pre2, pre1, "G") % MOD + rec(i + 1, pre2, pre1,
                                                    "T") % MOD
        elif pre1 == "C" and pre2 == "A":
            ret = rec(i + 1, pre2, pre1, "C") % MOD + rec(
                i + 1, pre2, pre1, "A") % MOD + rec(i + 1, pre2, pre1,
                                                    "T") % MOD
        elif pre3 == "A" and pre1 == "G":
            ret = rec(i + 1, pre2, pre1, "A") % MOD + rec(
                i + 1, pre2, pre1, "G") % MOD + rec(i + 1, pre2, pre1,
                                                    "T") % MOD
        elif pre3 == "A" and pre2 == "G":
            ret = rec(i + 1, pre2, pre1, "A") % MOD + rec(
                i + 1, pre2, pre1, "G") % MOD + rec(i + 1, pre2, pre1,
                                                    "T") % MOD
        else:
            ret = rec(i + 1, pre2, pre1,
                      "A") + rec(i + 1, pre2, pre1, "G") % MOD + rec(
                          i + 1, pre2, pre1, "C") % MOD + rec(
                              i + 1, pre2, pre1, "T") % MOD
        ret %= MOD
        memo[(i, pre1, pre2, pre3)] = ret
        return ret


# 最初とりうるやつ（めんどい）
ans = 0
for i in ["A", "G", "C", "T"]:
    for j in ["A", "G", "C", "T"]:
        for k in ["A", "G", "C", "T"]:
            ans += rec(0, i, j, k)

print((ans % MOD))


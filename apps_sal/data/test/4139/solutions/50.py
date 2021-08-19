# わからなかったので答えを見た
# 実装の仕方や、考え方を復習してもう一回やってみる

N = int(input())


def solve(s):
    # ベースケース
    if int(s) > N:
        return 0
    # s.countでsに357のうちどれかが入っていることを確かめる 真なら1で偽なら0
    ret = 1 if all(s.count(i) > 0 for i in '357') else 0

    # 再帰する
    for c in '753':
        ret += solve(s + c)

    return ret


print((solve("0")))

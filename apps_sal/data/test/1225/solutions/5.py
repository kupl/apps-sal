H = int(input())

# 体力がHのモンスター1体に勝つために必要な攻撃回数をf(H)とする
# すると、f(H)は以下の漸化式に従って求まる
# f(H)=2*f(floor(H/2)+1) (H>1)
# f(H)=1 (H=1)

# 漸化式の実装はAtCoderで珍しい。パターンとして覚えよ！


def attack_num(x):
    if x == 1: return 1
    else: return 2 * attack_num(x // 2) + 1


print(attack_num(H))

# 高橋君のモンスターは体力が A で攻撃力が B
# 青木君のモンスターは体力が C で攻撃力が D
# モンスターの体力が 0 以下になった方の負け、
# 高橋君が勝つなら Yes、負けるなら No を出力

A, B, C, D = map(int, input().split())

while A > 0 and C > 0:
    C -= B
    if C <= 0:
        print('Yes')
        break
    A -= D
    if A <= 0:
        print('No')
        break

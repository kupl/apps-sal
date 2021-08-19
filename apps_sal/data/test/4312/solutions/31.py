# 高橋君のモンスター　体力A、攻撃力B
# 青木君のモンスター　体力C、攻撃力D
# 高橋->青木->高橋->青木->...の順に攻撃する
# 高橋勝つならYes、負けるならNo

a, b, c, d = map(int, input().split())

while a > 0 and c > 0:
    c -= b
    if c <= 0:
        print("Yes")
        break

    a -= d
    if a <= 0:
        print("No")
        break

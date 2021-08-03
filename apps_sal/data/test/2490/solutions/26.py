n = "0" + input()  # 文字列として受け取り
N = len(n)
plus = 1
just = 0
for i in range(1, N):
    # 前の桁がplusだった場合の最低枚数を計算する
    plus_plus = plus + 10 - (int(n[i]) + 1)  # この桁も１枚多く払う
    plus_just = plus + 10 - int(n[i])  # この桁はちょうど払う
    # 前の桁はちょうど払っていた場合
    just_plus = just + 1 + int(n[i])  # この桁は１枚多く払う
    just_just = just + int(n[i])  # この桁もちょうど払う

    plus = min(plus_plus, just_plus)
    just = min(just_just, plus_just)

# 最後の桁は1枚余分に払う必要がない
print(just)

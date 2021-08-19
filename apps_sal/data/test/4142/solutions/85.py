# Ｓを入力する
S = input()

# forループでタプルの要素を奇数番目と偶数番目で分ける
even = []
odd = []
for i in range(len(S)):
    if i % 2 == 0:
        even.append(S[i])
    else:
        odd.append(S[i])

# 奇数番目が全てR,U,Dか確認する
# 偶数番目がすべてL,U,Dか確認する
# ↑がTrueだったらYes,そうでないならNoを出力する

if "L" not in even and "R" not in odd:
    print("Yes")
else:
    print("No")

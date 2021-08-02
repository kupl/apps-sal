s = input()
t = input()
# s,tをリストにする
s = list(s)
t = list(t)

# 変数count,judgementに0を代入
count = 0
judgment = 0

# sの長さだけ順番入れ替えを繰り返し
while count <= len(s):
    item = s.pop()
    s.insert(0, item)
    if s == t:
        # s==tになったらjudgmentでカウントアップ
        judgment += 1
    # 回数をカウントアップ
    count += 1

# 一回もs==tになってなければNo
if judgment == 0:
    print("No")
else:
    print("Yes")

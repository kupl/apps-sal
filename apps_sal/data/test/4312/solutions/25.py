a,b,c,d = map(int,input().split())
# 高橋君の倒すまでの攻撃回数
takahashi_turn = 0
# 青木君の倒すまでの攻撃回数
aoki_turn = 0
# 攻撃するたびに回数カウントして体力を減らす
while c - b > 0:
    takahashi_turn += 1
    c -= b
while a - d > 0:
    aoki_turn += 1
    a -= d
# 高橋くんが早く倒すときはYes
if takahashi_turn <= aoki_turn:
    print("Yes")
else:
    print("No")

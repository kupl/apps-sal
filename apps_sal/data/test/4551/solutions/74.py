# A,B,C,Dのおもりの重さを整数で入力
A,B,C,D = map(int,input().split())
if A + B > C + D:
# 左の皿（A+B）の方が重いならLeft、同じならBalanced、左の皿（C+D）が重いならRightを出力
    print("Left")
elif A + B == C + D:
    print("Balanced")
else:
    print("Right")

# クッキー枚数（A,B）を整数で入力
A,B = map(int,input().split())
# AかBかA+Bのどれかを3匹に分けれればPossible、できなければImpossible
if A%3==0 or B%3==0 or (A+B)%3==0:
    print("Possible")
else:
    print("Impossible")

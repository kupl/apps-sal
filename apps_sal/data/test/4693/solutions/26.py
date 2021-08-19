# 入力
A, B = map(int, input().split())

# A+Bが10以上ならerror、それ以外なら結果を出力
if A + B >= 10:
    print('error')
else:
    print(A + B)

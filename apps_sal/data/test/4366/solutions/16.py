# 入力
A, B = map(int, input().split())

# 24時間表記に合わせて出力
if A + B > 23:
    print((A + B) % 24)
else:
    print(A + B)

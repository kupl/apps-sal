# 入力
A, B = map(int,input().split())

# 処理
start = A + B
if start >= 24:
    print(start - 24)
else:
    print(start)

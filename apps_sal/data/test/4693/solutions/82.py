# 入力
A, B =map(int,input().split())

# 処理
answer = A + B
if answer < 10:
    print(answer)
else:
    print('error')

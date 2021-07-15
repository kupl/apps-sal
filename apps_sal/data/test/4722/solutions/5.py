# 入力
A, B = map(int,input().split())

# 処理
if (A + B) % 3 == 0 or A % 3 == 0 or B % 3 == 0:
    print('Possible')
else:
    print('Impossible')

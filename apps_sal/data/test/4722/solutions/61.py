# 入力
A, B = map(int, input().split())

# 出力
if A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0:
    print('Possible')
else:
    print('Impossible')

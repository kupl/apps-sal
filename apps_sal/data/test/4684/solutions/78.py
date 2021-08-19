# 入力
r, g, b = map(int, input().split())

# 処理
answer = (r * 100 + g * 10 + b) % 4
if answer == 0:
    print('YES')
else:
    print('NO')

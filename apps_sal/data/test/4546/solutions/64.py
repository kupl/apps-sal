# 入力
a, b, c = map(int, input().split())

# 処理
if b - a == c - b:
    print('YES')
else:
    print('NO')

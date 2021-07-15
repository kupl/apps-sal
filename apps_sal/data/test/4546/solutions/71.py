# 入力
a, b, c = map(int, input().split())

# 出力
if b - a == c - b:
    print('YES')
else:
    print('NO')

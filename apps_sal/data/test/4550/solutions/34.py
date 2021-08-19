# 入力
a, b, c = map(int, input().split())

# 出力
if a == b + c or b == a + c or c == a + b:
    print('Yes')
else:
    print('No')

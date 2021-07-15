# 入力
a, b, c = map(int,input().split())

# 処理
if a == b + c or b == a + c or c == a + b:
    print('Yes')
else:
    print('No')

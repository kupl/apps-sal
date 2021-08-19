# 入力
a, b, c = map(int, input().split())

# 処理
if a + b == c:
    print('Yes')
elif a + c == b:
    print('Yes')
elif b + c == a:
    print('Yes')
else:
    print('No')

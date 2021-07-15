# 入力
a, b, c = list(map(int, input().split()))

# 処理
if a + b == c or b + c == a or c + a == b:
    print('Yes')

else:
    print('No')


# 出力



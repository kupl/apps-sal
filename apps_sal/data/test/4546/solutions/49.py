# 入力
a, b, c = map(int, input().split())

# b-a=c-bならYes、違うならNo
if b - a == c - b:
    print('YES')
else:
    print('NO')

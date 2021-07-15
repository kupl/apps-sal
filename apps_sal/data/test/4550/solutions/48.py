# A - キャンディーと2人の子供

# それぞれ数個ずつキャンディーの入ったパックが3個ある
# 二人の子供に、キャンディーを等しい数ずつ分けられるか判定する


a, b, c = list(map(int, input().split()))

if a + b == c \
or a + c == b \
or b + c == a:
    print('Yes')
else:
    print('No')


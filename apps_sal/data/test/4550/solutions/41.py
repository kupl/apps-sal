# 入力
a, b, c = list(map(int, input().split()))

# 2等分できるならYes、できないならNo
if a + b == c:
    print('Yes')
elif a + c == b:
    print('Yes')
elif b + c == a:
    print('Yes')
else:
    print('No')


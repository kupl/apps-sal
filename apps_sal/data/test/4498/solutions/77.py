a, b, c, d = list(map(int,input().split()))

# aとcの距離の絶対値ACを定義
if (a - c) >= 0:
    AC = (a-c)
else:
    AC = (c-a)

# BがAとCの間に入る場合のみ、AB間、BC間を定義
if a < b < c:
    AB = (b - a)
    BC = (c - b)
if c < b < a:
    AB = (a-b)
    BC = (b-c)

# AとCの距離がd以下ならYes！
if AC <= d:
    print('Yes')
# AB間、BC間ともにd以下ならYes！
elif AB <= d and BC <= d:
    print('Yes')
else:
    print('No')


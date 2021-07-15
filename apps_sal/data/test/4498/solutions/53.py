# Aさんは a[m] 地点、Bさんは b[m] 地点、Cさんは c[m] 地点
# 二人の人間は、距離が d[m] 以内のとき直接会話可能
# A・Cが直接的に会話ができる or A・Bさんが直接会話でき、かつB・Cが直接会話できる
# 会話できるなら Yes を, できないなら No を出力せよ。

a,b,c,d = map(int , input().split())
# print(a)
# print(b)
# print(c)
# print(d)

# aとcの差の絶対値がd以下
if abs(c-a) <= d:
    print('Yes')
# aとbの差の絶対値がd以下かつbとcの差の絶対値がd以下
elif abs(b-a) <= d and abs(c-b) <= d:
    print('Yes')
else:
    print('No') 

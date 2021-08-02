# Aさんは a[m]地点、Bさんは b[m]地点、Cさんは c[m]地点
# 2人の人間は、距離が d[m] 以内の時直接会話可能
# A・Cが直接的に会話できる or A・Bが直接会話でき、かつ B・Cが直接会話できる
# 会話できるなら Yes ,できないなら No を出力

a, b, c, d = map(int, input().split())
# print(a)
# print(b)
# print(c)
# print(d)


# a と c の差の絶対値が d 以下
if abs(c - a) <= d:
    print('Yes')
# a と b の差の絶対値が d 以下かつ b と c 野さの絶対値が d 以下
elif abs(b - a) <= d and abs(c - b) <= d:
    print('Yes')
else:
    print('No')

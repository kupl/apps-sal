# 1回a円で聞ける
# b円持っている。c回聴くと満足するので、最大c回まで聞けるだけ聞く
# a円 * c回が b円以下の場合
a,b,c = map(int, input().split())
if a * c <= b:
    print(c)
# a円 * c回 が b円を上回る場合
# b円以下に収まる回数までしか聞けない
if a * c > b:
    print(b // a)

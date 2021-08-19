a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

# 最長距離がk以下ならば、全てのアンテナが直接通信できる
# 直接通信できないアンテナの組は存在しない => Yay! を出力
# 最長距離がkより大きいならば、直接通信できないアンテナの組は少なくとも1つ存在する
if e - a <= k:
    print('Yay!')
else:
    print(':(')

n,k,m = map(int,input().split())
a = list(map(int,input().split()))

# 満点Kをとっても平均ｍにならないときには-1
if m > (sum(a) + k) / (len(a) + 1):
    print(-1)
# 0点をとっても平均ｍ以上になるときには０
elif m < (sum(a)) / (len(a) + 1):
    print(0)
# 上記で無い場合には平均ｍとなる整数を出力
else:
    print((m * (len(a) + 1)) - sum(a) )

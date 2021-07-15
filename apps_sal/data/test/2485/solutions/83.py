import collections

h,w,m = map(int,input().split())
X = []
Y = []
for _ in range(m):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
#まず一番大いX座標を調べる
most_common_x = collections.Counter(X).most_common()
most_common_x_index = most_common_x[0][0] #x座標
most_common_x_count = most_common_x[0][1] #その線に存在する爆弾の個数
#爆破されない座標たちの共通するY座標を探す
otherwise = []
for i in range(m):
    if X[i] != most_common_x_index:#not most common
        otherwise.append(Y[i])
most_common_y = collections.Counter(otherwise).most_common()
if len(most_common_y)!= 0: #ある特定のyが存在した時
    ansx = most_common_y[0][1] + most_common_x_count
else: #もともと全部のy座標が揃っていた時
    ansx = most_common_x_count
#次にY座標を基準にして調べる
most_common_y = collections.Counter(Y).most_common()
most_common_y_index = most_common_y[0][0] #x座標
most_common_y_count = most_common_y[0][1] #その線に存在する爆弾の個数
otherwise = []
for i in range(m):
    if Y[i] != most_common_y_index:#not most common
        otherwise.append(X[i])
most_common_x = collections.Counter(otherwise).most_common()
if len(most_common_x)!= 0 :
    ansy = most_common_x[0][1] + most_common_y_count
else:
    ansy = most_common_y_count
print(max(ansx,ansy))

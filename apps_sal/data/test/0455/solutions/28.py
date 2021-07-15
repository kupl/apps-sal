N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]


#合計が偶数or奇数のどちらかだけしかできない
if N != 1:
    a = abs(XY[0][0]) + abs(XY[0][1])
    flag = (XY[0][0] + XY[0][1])%2
for i in range(N-1):
    b = abs(XY[i+1][0]) + abs(XY[i+1][1])
    a = max(a, b)
    if flag != (XY[i+1][0] + XY[i+1][1])%2:
        print((-1))
        return

#必要な桁数の確認
m = 0
while a > 1:
    m += 1
    a = a//2

#腕の長さを求める
d = []
for i in range(m+3, -1, -1):
    d += [2 ** i]

if flag == 0: #偶数の場合一つずらすための1を加える
    print((len(d) + 1))
    print((' '.join(map(str, [1] + d))))
else: #奇数の場合そのまま出力
    print((len(d)))
    print((' '.join(map(str, d))))
#ここまでで、腕の長さが決定
#これ以降で各X, Yに対する答えを見つける。

def string(X, Y): #あるXYに対して動かし方を返す
    if (abs(X) + abs(Y))%2 == 0: #偶数のとき
        ans = 'R'
        x = X - 1
        y = Y
    else:
        x, y = X, Y
        ans = str()
    for i in d:
        if abs(x - i) + abs(y) < i:
            ans += 'R'
            x = x - i
        elif abs(x + i) + abs(y) < i:
            ans += 'L'
            x = x + i
        elif abs(x) + abs(y - i) < i:
            ans += 'U'
            y = y - i
        elif abs(x) + abs(y + i) < i:
            ans += 'D'
            y = y + i
    return ans

for i in XY:
    print((string(i[0], i[1])))
# print (string(XY[0][0], XY[0][1]))
# print (string(XY[1][0], XY[1][1]))
# print (string(XY[2][0], XY[2][1]))
# print (string(XY[3][0], XY[3][1]))


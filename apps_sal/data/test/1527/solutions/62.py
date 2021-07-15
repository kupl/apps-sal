#import sys
#input=sys.stdin.readline()
#print(input)

#import pprint
h,w = map(int,input().split())
s = [list(input())for i in range(h)]
#print("s")
#pprint.pprint(s,width=w*10)

visited = [[0 for i in range(w)] for j in range(h)]#sと同じ形に0を配置した表
quene = []#移動元Nowとなることができる座標のリスト
ans = 0

for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            quene.append([i,j])#スタート地点をQueneに追加
            visited[i][j]=1#スタート地点を1にする
#            print("visited")
#            pprint.pprint(visited,width=w*10)
#            print(quene)

            dy_dx=[[1,0],[-1,0],[0,1],[0,-1]]#１回に移動出来る量

            while len(quene)>=1:
                now=quene.pop(0)#queneの左端の項を取り出す
#                print(now)
                for k in range(4):
                    y=now[0]+dy_dx[k][0]#nowから移動先[x,y]へのy軸方向の移動量
                    x=now[1]+dy_dx[k][1]#nowから移動先[x,y]へのx軸方向の移動量
                    if 0<=y<h and 0<=x<w:#移動先が表を飛び出していなければOK
                        if s[y][x]!="#" and visited[y][x]==0:#移動先が壁でない、かつ行ったことがなければOK
                            visited[y][x]=visited[now[0]][now[1]]+1#移動先の値をNowの値+1にする
                            quene.append([y,x])#Queneに移動先座標を追加
#                           pprint.pprint(visited,width=w*10)
#       一つのスタート地点から幅優先探索を終わらせたら、移動量の最大値を求める
        for l in range(h):
            for m in range(w):
                ans = max(ans,visited[l][m])#これまでの最大値と今回得られた移動量の最大値を比較し、大きいほうを新しい答えにする
        visited = [[0 for i in range(w)] for j in range(h)]#visited初期化
print(ans-1)

H, W, N = map(int, input().split())
from collections import defaultdict as dd
Grid =  dd(lambda:0) #3*3正方形を左上のマスで区別。値は正方形内の黒塗りの個数
Draw = lambda x,y:[(x-i,y-j) for i in range(3) for j in range(3) if 0<=x-i<H-2 and 0<=y-j<W-2] #塗りつぶしたマスを含む正方形の座標のリストを返す関数
for _ in range(N):
    a, b = map(int, input().split())
    for x,y in Draw(a-1,b-1): #Gridの更新
        Grid[x,y] += 1
Ans = [(H-2)*(W-2)-len(Grid) if i == 0 else sum(v==i for v in Grid.values()) for i in range(10)]         
for ans in Ans:
    print(ans)

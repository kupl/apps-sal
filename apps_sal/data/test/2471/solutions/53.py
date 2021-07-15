H, W, N = map(int, input().split())
Draw = [tuple(map(int, input().split())) for _ in range(N)]
from collections import defaultdict as dd
Sq =  dd(lambda:0) #3*3正方形を左上のマスの座標で区別。値は正方形内の黒塗りの個数
In = lambda x,y:[(x-i,y-j) for i in range(3) for j in range(3) if 0<=x-i<H-2 and 0<=y-j<W-2] #塗りつぶしたマスを含む正方形の座標のリストを返す関数
for a,b in Draw:
    for x,y in In(a-1,b-1): 
        Sq[x,y] += 1 #Sqの更新
Ans = [(H-2)*(W-2)-len(Sq)] + [sum(v==i for v in Sq.values()) for i in range(1,10)]         
for ans in Ans:
    print(ans)

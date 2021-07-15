def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
              #if (d[i][k] != float("INF")) and (d[k][j] != float("INF")):
                d[i][j] = min(d[i][k] + d[k][j], d[i][j])
                
        #print(d)
    return d

##############################
n,m = list(map(int,input().split())) #n:頂点数　m:辺の数

d = [[float("INF")] * n for i in range(n)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)

hen = [0] * m
for i in range(m):
    x,y,z = list(map(int,input().split()))
    d[x - 1][y - 1] = z
    d[y - 1][x - 1] = z
    hen[i] = [x - 1, y - 1, z]
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０

ans = warshall_floyd(d)
#それぞれの出発地点ごとにmaxをとり、そのmaxが最小の地点に引っ越し
#そのときの所要時間がp
#print(used)
answer = 0
for i in range(m):
  now = hen[i]
  if d[now[0]][now[1]] != now[2]:
    answer += 1
  
print(answer)  



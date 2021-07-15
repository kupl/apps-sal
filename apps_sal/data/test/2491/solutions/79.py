INF = 10**30
import sys
sys.setrecursionlimit(10**6)
def bellman_ford(s, t, g):
    d = [INF for _ in range(n)] # 各頂点への最小コスト
    d[s] = 0 # 自身への距離は0
    val_at_t = INF # 下記参照
    for i in range(n):
        #update = False # 更新が行われたか
        for x, y, z in g:
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                #update = True
        # 負閉路が存在して、点tの値が更新され続けている場合
        if i == n-1 and val_at_t > d[t]:
            return []
        val_at_t = d[t] #点tの現在の値
    return d

n, m = list(map(int, input().split())) # n:頂点数, m:辺の数
g = []
for _ in range(m):
    x, y, z = list(map(int, input().split())) # 始点,終点,コスト
    x -= 1
    y -= 1
    z *= -1
    g.append([x, y, z])
    
ans = bellman_ford(0, n-1, g)
#print(ans)
print((-ans[n-1] if ans else "inf"))


import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = list(map(int, input().split()))
abc = [tuple(map(int,input().split())) for i in range(m)]
es = []
for a,b,c in abc:
    a,b = a-1,b-1
    es.append((a,b,c))

INF = float('inf')

def find_negative_loop(n,es,s):
    #負の経路の検出
    #n:頂点数, es[i]: [辺の始点,辺の終点,辺のコスト], s:始点
    dist = [-INF] * n
    dist[s] = 0

    for i in range(n):
        for a,b,c in es:
            if dist[b] < dist[a]+c:
                dist[b] = dist[a]+c
                # if i == n-1: # n回目にも更新が行われている場合，ループが存在する
                if i == n-1 and b==n-1: # 終点に影響を及ぼすループが存在する
                        return INF
    return dist[n-1]

ans = find_negative_loop(n,es,0)

if ans == INF:
    print('inf')
    return

print(ans)


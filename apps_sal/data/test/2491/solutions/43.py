INF = float('inf')
class BellmanFord:
    
    def bellmanford(self,s,V,E):
        dist = [INF for _ in range(V)]
        dist[s] = 0
        for i in range(V):
            for e in E:
                u,v,cost = e
                if dist[u] != INF and dist[v] > dist[u] + cost:
                    dist[v] = dist[u]+cost
                    if i == V-1 and v == V-1:
                        return -1
        return dist
    

def main():
    N,M = map(int,input().split())
    E = []
    for _ in range(M):
        a,b,c = map(int,input().split())
        a -= 1
        b -= 1
        E.append((a,b,-c))
    bf = BellmanFord()
    dist = bf.bellmanford(0,N,E)
    if dist == -1:
        print('inf')
    else:
        ans = dist[-1]
        print(-ans)

def __starting_point():
    main()
__starting_point()

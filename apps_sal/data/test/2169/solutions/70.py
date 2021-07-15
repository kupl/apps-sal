
def main():
    H, W, D = map(int, input().split())
    coordinate = [None] * (H*W)
    for i in range(H):
        for j, A in enumerate(list(map(int, input().split()))):
            coordinate[A-1] = (i, j)
    
    cost = [0] * (H*W)
    dist = lambda X, Y: abs(X[0]-Y[0]) + abs(X[1]-Y[1])
    for i in range(D, H*W):
        u,v = divmod(i, D)
        cost[i] = cost[i-D] + dist(coordinate[i], coordinate[i-D])

    Q = int(input())
    query = [tuple(map(int, input().split())) for _ in range(Q)]
    for l, r in query:
        print(cost[r-1]-cost[l-1])

main()

H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

x = [0]*(H*W+1)
p = [[] for _ in range(H*W+1)]

for h in range(H):
    for w in range(W):
        p[A[h][w]] = [h, w]

for i in range(D+1, H*W+1):
    x[i] = x[i-D]+abs(p[i][0]-p[i-D][0])+abs(p[i][1]-p[i-D][1])

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(x[r]-x[l])

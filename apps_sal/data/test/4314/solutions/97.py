H, W = map(int, input().split())
G = [list(input()) for i in range(H)]
allwhite = ['.'] * W
tmp = []
for i in range(H):
    if G[i] != allwhite:
        tmp.append(G[i])
G = tmp
ans = ["" for i in range(len(G))]
for j in range(W):
    p = False
    for i in range(len(G)):
        if G[i][j] == '
        p = True
        break
    if p:
        for i in range(len(G)):
            ans[i] += G[i][j]
print(*ans, sep='\n')

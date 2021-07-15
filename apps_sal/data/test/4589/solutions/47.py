H, W = (int(x) for x in input().split())
S = [input() for _ in range(H)]
ans = [''] * H  
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            ans[i] += '#'
            continue
        bom = 0
        for k in range(3):
            for l in range(3):
                if 0 <= i-1+k < H and 0 <= j-1+l < W:
                    if S[i-1+k][j-1+l] == '#':
                        bom += 1
        ans[i] += str(bom)
for s in ans:
    print(s)
                    


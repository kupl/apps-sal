#6 B - Minesweeper
H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]

dh = [0,1,0,-1,1,-1,1,-1]
dw = [1,0,-1,0,1,-1,-1,1]

for h in range(H):
    for w in range(W):
        #マス(h,w)について
        if S[h][w] == '#':
            continue
        else:
            cnt= 0
            for v in range(8):
                nxt_h = h + dh[v]
                nxt_w = w + dw[v]
                if not(-1<nxt_h<H) or not(-1<nxt_w<W):
                    continue
                elif S[nxt_h][nxt_w] == '#':
                    cnt += 1
                S[h][w] = str(cnt)
if H==1 and W==1:
    print(0)
else:
    for i in S:
        print(''.join(i))

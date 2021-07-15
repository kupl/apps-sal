H, W, M = map(int, input().split())
 
hs = [0] * H
ws = [0] * W
boms = set()
 
for i in range(M):
    r,c = map(int, input().split())
    r -= 1
    c -= 1
 
    hs[r] += 1
    ws[c] += 1
    boms.add((r, c))
mh, mw = 0, 0
for i in range(H):
    mh = max(mh, hs[i])
for j in range(W):
    mw = max(mw, ws[j])
max_h_list = []
max_w_list = []
    
for i in range(H):
    if hs[i] == mh: max_h_list.append(i)    
for j in range(W):
    if ws[j] == mw: max_w_list.append(j)
ans = mh + mw
 
for i in max_h_list:
    for j in max_w_list:
        if (i,j) not in boms:
            print(ans)
            return
print(ans-1) 

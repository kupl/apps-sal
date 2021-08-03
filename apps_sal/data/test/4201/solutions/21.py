H, W, K = map(int, input().split())
c = [list(input())for i in range(H)]
ans = 0
for i in range(1 << H):
    mh = []
    for j in range(H):
        if i & (1 << j):
            mh.append(j)
    mh = set(mh)
    for j in range(1 << W):
        mw = []
        for k in range(W):
            if j & (1 << k):
                mw.append(k)
        mw = set(mw)
        count = 0
        for a in range(H):
            for b in range(W):
                if not a in mh and not b in mw and c[a][b] == '#':
                    count += 1
        if count == K:
            ans += 1
print(ans)

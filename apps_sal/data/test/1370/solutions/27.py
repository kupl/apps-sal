H,W,K = map(int,input().split())
S = [input() for i in range(H)]

ans = H+W+9999
for b in range(1<<(H-1)):
    mp = [0]
    k = 0
    for i in range(H-1):
        if b&(1<<i):
            k += 1
        mp.append(k)
    tmp = bin(b).count('1')
    ws = [0] * H
    muri = False
    for col in zip(*S):
        for i,c in enumerate(col):
            if c == '1':
                ws[mp[i]] += 1
        if any(w > K for w in ws):
            ws = [0] * len(mp)
            for i,c in enumerate(col):
                if c == '1':
                    ws[mp[i]] += 1
            if any(w > K for w in ws):
                muri = True
                break
            tmp += 1
        if muri:
            break
    if not muri:
        ans = min(ans, tmp)
print(ans)

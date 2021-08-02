N, A, B, C = map(int, input().split())
L = [int(input()) for i in range(N)]

ans = float('inf')
for a in range(1 << N):
    at = []
    for i in range(N):
        if a & (1 << i):
            at.append(L[i])
    if not at: continue
    ap = 10 * (len(at) - 1) + abs(A - sum(at))
    for b in range(1 << N):
        if a & b: continue
        bt = []
        for i in range(N):
            if b & (1 << i):
                bt.append(L[i])
        if not bt: continue
        bp = 10 * (len(bt) - 1) + abs(B - sum(bt))
        for c in range(1 << N):
            if (a & c) or (b & c): continue
            ct = []
            for i in range(N):
                if c & (1 << i):
                    ct.append(L[i])
            if not ct: continue
            cp = 10 * (len(ct) - 1) + abs(C - sum(ct))
            ans = min(ans, ap + bp + cp)
print(ans)

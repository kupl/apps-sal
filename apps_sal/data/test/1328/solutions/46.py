N, Ma, Mb = list(map(int, input().split()))
D = [tuple(map(int, input().split())) for _ in range(N)]

def listup(L, D):
    for a, b, c in D:
        for (ka, kb), kc in L.copy().items():
            key = (ka+a, kb+b)
            L[key] = min(L[key], kc+c) if key in L else kc+c
        

L1 = {(0,0):0}
L2 = {(0,0):0}
listup(L1, D[:N//2])
listup(L2, D[N//2:])

ans = 10**9
for m in range(1,401):
    ma = Ma * m
    mb = Mb * m
    if ma>400 or mb>400: break
    for key1 in L1:
        ta1, tb1 = key1
        ta2 = ma - ta1
        tb2 = mb - tb1
        key2 = (ta2, tb2)
        if key2 in L2: ans = min(ans, L1[key1]+L2[key2])

print(ans if ans!=10**9 else -1)

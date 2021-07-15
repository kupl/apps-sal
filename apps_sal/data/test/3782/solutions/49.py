N, K, Q = map(int, input().split())
A = [int(a) for a in input().split()]
S = set(A)
I = sorted(list(S))
m = len(I)
D = {a: i for i, a in enumerate(I)}
ans = 1 << 30
for i in range(m):
    l = I[i]
    LL = []
    L = []
    for a in A:
        if a < l:
            if L:
                if len(L) >= K:
                    LL += sorted(L)[:len(L) - K + 1]
                L = []
        else:
            L.append(a)
    if L:
        if len(L) >= K:
            LL += sorted(L)[:len(L) - K + 1]
    if len(LL) >= Q:
        ans = min(ans, sorted(LL)[Q-1] - l)
print(ans)

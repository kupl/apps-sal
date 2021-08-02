import heapq as hp
import sys
input = sys.stdin.readline

N, K, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
Xs = sorted(list(set(A)))

ans = 10**14
for x in Xs:
    Ps = []
    tmp = []
    for a in A:
        if a >= x:
            tmp.append(a)
        else:
            if len(tmp) >= K:
                Ps.append(tmp)
            tmp = []
    if len(tmp) >= K:
        Ps.append(tmp)
    q = []
    for P in Ps:
        P.sort()
        for i, p in enumerate(P):
            q.append(p)
            if len(P) - K - i == 0: break
    if len(q) < Q:
        break
    q.sort()
    ans = min(ans, q[Q - 1] - x)

print(ans)

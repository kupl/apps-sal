from collections import Counter
(N, K) = list(map(int, input().split()))
TD = [tuple(map(int, input().split())) for _ in range(N)]
TD.sort(reverse=True, key=lambda a: a[1])
A = TD[:K]
B = []
V = set()
for (t, d) in TD:
    if t in V:
        continue
    B.append((t, d))
    V.add(t)
cntT = Counter([t for (t, _) in A])
V = set(cntT.keys())
S = sum([d for (_, d) in A])
B = [(t, d) for (t, d) in B if not t in V]
C = []
for (t, d) in A[::-1]:
    if cntT[t] > 1:
        C.append((t, d))
        cntT[t] -= 1
C = C[::-1]
ans = S + len(V) ** 2
for (t, d) in B:
    if not C:
        break
    (_, less) = C.pop()
    S -= less
    S += d
    V.add(t)
    ans = max(ans, S + len(V) ** 2)
print(ans)

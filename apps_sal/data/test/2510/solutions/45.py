(N, M) = (int(d) for d in input().split())
C = [set() for i in range(N + 1)]
for i in range(M):
    (A, B) = (int(d) for d in input().split())
    C[A].update([B])
    C[B].update([A])
seen = set()
G = []
for i in range(1, N + 1):
    if i in seen:
        continue
    G.append(set())
    Q = [i]
    G[-1].update(Q)
    seen.update(Q)
    while len(Q) > 0:
        I = Q.pop(0)
        J = C[I].difference(seen)
        Q += list(J)
        G[-1].update(J)
        seen.update(J)
print(max([len(g) for g in G]))

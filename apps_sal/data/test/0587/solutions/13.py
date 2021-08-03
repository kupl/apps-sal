N, K = map(int, input().split())
TD = [tuple(map(int, input().split())) for _ in range(N)]
M = len(set([t for t, d in TD]))

TD.sort(key=lambda x: x[1], reverse=True)
p, S, V = 0, [], set()
for t, d in TD[:K]:
    p += d
    if t in V:
        S.append(d)
    else:
        V.add(t)
p += len(V) ** 2
ans = p
for t, d in TD[K:]:
    if len(S) == 0:
        break
    if t not in V:
        p += 2 * len(V) + 1 - S.pop() + d
        V.add(t)
        ans = max(ans, p)
print(ans)

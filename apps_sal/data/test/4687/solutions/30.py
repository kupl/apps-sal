N, K = map(int, input().split())
d = {}
key = set([])
for _ in range(N):
    a, b = map(int, input().split())
    if a in key:
        d[str(a)] += b
    else:
        key.add(a)
        d[str(a)] = b
key = sorted(list(key))
for k in key:
    if d[str(k)] < K:
        K -= d[str(k)]
    else:
        print(k)
        break

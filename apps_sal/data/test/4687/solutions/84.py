N, K = map(int, input().split())
d = {}
for i in range(N):
    a, b = map(int, input().split())
    d[a] = d.get(a, 0) + b

cnt = 0
for k in sorted(d.keys()):
    cnt += d[k]
    if cnt >= K:
        print(k)
        break

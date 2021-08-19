(n, k) = map(int, input().split())
d = {}
for _ in range(n):
    (a, b) = map(int, input().split())
    if a in d.keys():
        d[a] += b
    else:
        d[a] = b
cnt = 0
sorted_d = sorted(d.items(), key=lambda x: x[0])
for (key, val) in sorted_d:
    cnt += val
    if k <= cnt:
        print(key)
        break

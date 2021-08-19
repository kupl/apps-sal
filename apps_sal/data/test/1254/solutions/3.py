(n, m) = list(map(int, input().split()))
spec = {}
for i in range(n):
    (s, r) = list(map(int, input().split()))
    if s in spec:
        spec[s].append(r)
    else:
        spec[s] = [r]
f = n
cnt = [-1 for i in range(n + 1)]
for (k, cur) in list(spec.items()):
    cur.sort(reverse=True)
    for j in range(1, len(cur)):
        cur[j] += cur[j - 1]
    for j in range(1, len(cur) + 1):
        if cnt[j] == -1:
            cnt[j] = 0
        cnt[j] += max(0, cur[j - 1])
print(max(cnt))

from collections import defaultdict
(n, m) = map(int, input().split())
cats = list(map(int, input().split()))
tree = defaultdict(list)
vst = [0] * n
for _ in range(n - 1):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)
ans = 0
vst[0] = True
Q = [(0, 0)]
while Q:
    (now, cc) = Q.pop()
    vst[now] = True
    cc = 0 if not cats[now] else cc + 1
    if cc > m:
        continue
    if now not in tree or all((vst[nxt] for nxt in tree[now])):
        if cc <= m:
            ans += 1
    for nxt in tree[now]:
        if not vst[nxt]:
            Q.append((nxt, cc))
print(ans)

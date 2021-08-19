from collections import deque
(N, M) = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
umami = [[] for _ in range(N + 1)]
for (a, b) in AB:
    umami[a].append(b)
    umami[b].append(a)
umaaji = [0] * (N + 1)
d = deque([1])
while d:
    r = d.popleft()
    for u in umami[r]:
        if umaaji[u] == 0:
            umaaji[u] = r
            d.append(u)
print('Yes')
for u in umaaji[2:]:
    print(u)

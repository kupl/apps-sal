import heapq as hq
(N, H) = map(int, input().split())
slash = 0
Throw = []
for _ in range(N):
    (a, b) = map(int, input().split())
    slash = max(slash, a)
    if b > a:
        Throw.append(b)
Throw = [-th for th in Throw if th > slash]
hq.heapify(Throw)
(dmg, cnt) = (0, 0)
while len(Throw) != 0:
    if dmg >= H:
        break
    dmg += -hq.heappop(Throw)
    cnt += 1
if dmg < H:
    from math import ceil
    cnt += ceil((H - dmg) / slash)
print(cnt)

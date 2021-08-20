from collections import deque
(n, d, a) = map(int, input().split())
hit = []
for i in range(n):
    (x, h) = map(int, input().split())
    hit.append([x, h])
hit.sort()
que = []
ans = 0
bomb = 0
for i in range(n):
    while True:
        if len(que) == 0:
            break
        if hit[i][0] <= que[0][0]:
            break
        bomb -= que[0][1]
        que.pop(0)
    r = hit[i][1] - bomb
    if r < 0:
        continue
    c = (r + a - 1) // a
    ans += c
    bomb += c * a
    que.append((hit[i][0] + 2 * d, c * a))
print(ans)

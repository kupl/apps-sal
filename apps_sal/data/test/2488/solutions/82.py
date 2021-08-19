from heapq import heappush, heappop
(n, d, a) = list(map(int, input().split()))
actions = []
for _ in range(n):
    (x, h) = list(map(int, input().split()))
    heappush(actions, (x, 0, (h + a - 1) // a))
cnt = 0
bomb = 0
current_bomb = 0
while cnt < n:
    (a, c, b) = heappop(actions)
    if c:
        current_bomb -= b
        continue
    else:
        HP = b
        if HP <= current_bomb:
            cnt += 1
            continue
        else:
            HP -= current_bomb
            cnt += 1
            current_bomb += HP
            bomb += HP
            heappush(actions, (a + 2 * d, 1, HP))
print(bomb)

from collections import deque
N, D, A = list(map(int, input().split()))
pair_xh = [[-1, -1] for _ in range(N)]
for i in range(N):
    pair_xh[i][0], pair_xh[i][1] = list(map(int, input().split()))
pair_xh.sort(key=lambda x: x[0])

q_lim_d = deque()
total = 0
count = 0
for i in range(N):
    x = pair_xh[i][0]
    h = pair_xh[i][1]

    while len(q_lim_d) and q_lim_d[-1][0] < x:
        total -= q_lim_d[-1][1]
        q_lim_d.pop()
    h -= total
    if h > 0:
        times = (h + A - 1) // A
        count += times
        damage = A * times
        total += damage
        q_lim_d.appendleft([x + 2 * D, damage])
print(count)

from collections import deque
N, C = list(map(int, input().split()))
que = []
Que = []
channel = [[] for i in range(C+1)]
for i in range(N):
    s, t, c = list(map(int, input().split()))
    channel[c].append((s, t))
for i in range(C+1):
    channel[i].sort()
    tmp_que = deque(channel[i])
    left_que = deque([])
    if tmp_que:
        x, y = tmp_que.popleft()
        left_que.append((x, y))
        while tmp_que:
            lx, ly = left_que.pop()
            rx, ry = tmp_que.popleft()
            if ly == rx:
                left_que.append((lx, ry))
            elif ly < rx:
                left_que.append((lx, ly))
                left_que.append((rx, ry))
    for x, y in left_que:
        Que.append((2*x-1, 1))
        Que.append((2*y, -1))
ans = 0
value = 0
Que.sort(reverse=True)
while Que:
    v, command = Que.pop()
    value += command
    ans = max(ans, value)
print(ans)



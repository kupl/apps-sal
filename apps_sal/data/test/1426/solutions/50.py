from collections import deque

n, m = list(map(int, input().split()))
uv = [[] for _ in range(n)]
for _ in range(m):
    u, v = list(map(int, input().split()))
    uv[u - 1].append(v - 1)
s, t = list(map(int, input().split()))
s -= 1
t -= 1

queue = deque()
queue.append(s)
queue.append(1)
queue.append(0)
check = [[False for _ in range(3)] for _ in range(n)]
check[s][0] = True

while queue:
    pos = queue.popleft()
    ans = queue.popleft()
    kkp = queue.popleft()
    for next_pos in uv[pos]:
        if next_pos == t and kkp == 2:
            print((ans // 3))
            return
        if check[next_pos][(kkp + 1) % 3]:
            continue
        check[next_pos][(kkp + 1) % 3] = True
        queue.append(next_pos)
        queue.append(ans + 1)
        queue.append((kkp + 1) % 3)
print((-1))

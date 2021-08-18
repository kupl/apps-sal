from collections import deque
import sys

H, W = map(int, input().split())
S = [[x for x in input()] for _ in range(H)]

count = 0
for i in range(len(S)):
    count += S[i].count('.')

d = deque([(0, 0)])
distance = [[-1] * W for _ in range(H)]
distance[0][0] = 0
goal_distance = 0

while d:
    h, w = d.popleft()
    if h == H - 1 and w == W - 1:
        goal_distance = distance[h][w]
        break

    if h - 1 >= 0 and S[h - 1][w] == '.':
        d.append((h - 1, w))
        distance[h - 1][w] = distance[h][w] + 1
        S[h - 1][w] = '#'

    if h + 1 <= H - 1 and S[h + 1][w] == '.':
        d.append((h + 1, w))
        distance[h + 1][w] = distance[h][w] + 1
        S[h + 1][w] = '#'

    if w - 1 >= 0 and S[h][w - 1] == '.':
        d.append((h, w - 1))
        distance[h][w - 1] = distance[h][w] + 1
        S[h][w - 1] = '#'

    if w + 1 <= W - 1 and S[h][w + 1] == '.':
        d.append((h, w + 1))
        distance[h][w + 1] = distance[h][w] + 1
        S[h][w + 1] = '#'
else:
    if distance[H - 1][W - 1] == -1:
        print(-1)
        return

print(count - (goal_distance + 1))

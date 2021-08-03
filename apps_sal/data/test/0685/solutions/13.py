from collections import Counter, defaultdict, deque
def read(): return list(map(int, input().split()))


n, h = read()
dis = []
for _ in range(n):
    a, b = read()
    dis.append([a, b])

rec = []
for i in range(1, n):
    rec.append(dis[i][0] - dis[i - 1][1])
rec.append(float('inf'))

s = 0
left = h
i, j = 0, 0
res = 0
vis = [False] * n
while i < n:
    while j < n and left > 0:
        if not vis[j]:
            s += dis[j][1] - dis[j][0]
            vis[j] = True
        if left > rec[j]:
            left -= rec[j]
            s += rec[j]
            j += 1
        else:
            res = max(res, s + left)
            while i < n and left <= rec[j]:
                s -= dis[i][1] - dis[i][0] + rec[i]
                left += rec[i]
                i += 1
            if i >= n:
                break

print(res)

N = int(input())
d = []
visited = [False for _ in range(N + 1)]
for _ in range(N):
    d.append(int(input()) - 1)

i = 0
cnt = 0
while True:
    if i == 1:
        break
    elif cnt >= N:
        cnt = -1
        break
    elif visited[i]:
        cnt = -1
        break
    else:
        visited[i] = True
        cnt += 1
        i = d[i]

print(cnt)

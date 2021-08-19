s = int(input())
visited = [False] * (10 ** 6 + 1)
visited[s] = True
cnt = 1
while True:
    if s & 1:
        s = s * 3 + 1
    else:
        s //= 2
    cnt += 1
    if visited[s]:
        print(cnt)
        break
    visited[s] = True

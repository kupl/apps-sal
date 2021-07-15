# N<=10^5なので愚直にやっても間に合う
n = int(input())
a = [int(input()) - 1 for _ in range(n)]
visited = [False] * n
now = 0
count = 0
while visited[now] != True:
    count += 1
    visited[now] = True
    now = a[now]
    if now == 1:
        print(count)
        return
print((-1))


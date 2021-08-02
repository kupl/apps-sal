n = int(input())
p = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
ans = 0
visited = [False for i in range(n)]
for i in range(n):
    if visited[i]:
        continue
    ans += 1
    while not visited[i]:
        visited[i] = True
        i = p[i] - 1
if ans == 1:
    ans = 0
ans += (sum(b) + 1) % 2
print(ans)

n = int(input())
lst = [int(i) for i in input().split()]

visited = {}

for d in lst:
    if d in visited.keys():
        visited[d] += 1
    else:
        visited[d] = 1
count = 0
for d in visited.keys():
    count += int(visited[d] * (visited[d] - 1) / 2)
for d in lst:
    v = visited[d] - 1
    ans = count - v
    print(ans)

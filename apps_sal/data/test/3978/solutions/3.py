n = int(input())
l1 = list(map(int, input().split()))
ans = 0
l1.sort()
visited = [0] * n
for i in range(n):
    if visited[i] == 1:
        continue
    visited[i] = 1
    ans += 1
    for j in range(i + 1, n):
        if visited[j] == 0 and l1[j] % l1[i] == 0:
            visited[j] = 1
print(ans)

n, m = list(map(int, input().split()))
arr = [0] + list(map(int, input().split()))
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = list(map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

ans = 0
for i in range(1, n + 1):
    for j in g[i]:
        if arr[j] >= arr[i]:
            break
    else:
        ans += 1

print(ans)

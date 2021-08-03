n, m = map(int, input().split())
h = list(map(int, input().split()))
c = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    c[a].append(b)
    c[b].append(a)

ans = 0
for i in range(n):
    high = h[i]
    for j in c[i]:
        if h[j] >= high:
            break
    else:
        ans += 1
print(ans)

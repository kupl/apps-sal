# print(sum(map(lambda x: len(str(x).strip("47")) == 0, range(int(input()) + 1))))

n, m = map(int, input().split())
adj = [0 for _ in range(n + 1)]
cnt = [0 for _ in range(n + 1)]
x = map(int, input().split())
f1 = 0
x1 = next(x)
for i in range(m - 1):
    x2 = next(x)
    minx = min(x1, x2)
    maxx = x1 + x2 - minx
    x1 = x2
    dx = maxx - minx
    if dx > 0:
        adj[minx] += minx - 1
        adj[maxx] += minx - dx
        f1 += dx
        if dx >= 2:
            cnt[minx + 1] += 1
            cnt[maxx] -= 1
print(f1, end=' ')
c = cnt[1]
for i in range(2, n + 1):
    c += cnt[i]
    print(f1 - c + adj[i], end=' ')

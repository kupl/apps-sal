n = int(input())
points = []
cnt = {}
for i in range(n):
    x,y = list(map(int, input().split()))
    for a,b in points:
        u, v = x - a, y - b
        q = (u / v if v else int(2e9), u * u + v * v)
        cnt[q] = cnt.get(q,0) + 1
    points.append((x,y))

print(sum(k * k - k for k in list(cnt.values())) // 4)


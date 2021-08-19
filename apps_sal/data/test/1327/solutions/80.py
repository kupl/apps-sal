(n, m) = map(int, input().split())
cake = [[int(i) for i in input().split()] for _ in range(n)]
ans = 0
for sign_x in [1, -1]:
    for sign_y in [1, -1]:
        for sign_z in [1, -1]:
            point = []
            for (x, y, z) in cake:
                v = x * sign_x + y * sign_y + z * sign_z
                point.append(v)
            point.sort(reverse=True)
            ans = max(sum(point[:m]), ans)
print(ans)

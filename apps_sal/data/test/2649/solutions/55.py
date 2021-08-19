n = int(input())
xy_array = [list(map(int, input().split())) for _ in range(n)]
th = pow(10, 9)
z_max = -th
z_min = th
w_max = -th
w_min = th
for (x, y) in xy_array:
    z_max = max(x + y, z_max)
    z_min = min(x + y, z_min)
    w_max = max(x - y, w_max)
    w_min = min(x - y, w_min)
ans = max(z_max - z_min, w_max - w_min)
print(ans)

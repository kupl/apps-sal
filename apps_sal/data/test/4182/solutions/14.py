n, m, x, y = map(int, input().split())
max_x = max(list(map(int, input().split())))
min_y = min(list(map(int, input().split())))

for z in range(x + 1, y + 1):
    if max_x < z <= min_y:
        print("No War")
        return
else:
    print("War")

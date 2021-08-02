n, m, x, y = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
max_x = max(a)
min_y = min(b)
max_x = max(max_x, x)
min_y = min(min_y, y)

if max_x < min_y:
    print("No War")
else:
    print("War")

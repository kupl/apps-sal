W, H, x, y = map(int, input().split())

if W / 2 == x and H / 2 == y:
    a = 1
else:
    a = 0

print(W * H / 2, a)

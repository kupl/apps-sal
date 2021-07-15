W, H, x, y = map(int, input().split())

if W == 2 * x and H == 2 * y:
    print(W*H/2, 1)
else:
    print(W*H/2, 0)

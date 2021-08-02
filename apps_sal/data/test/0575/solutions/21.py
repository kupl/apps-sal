def quadrant(x, y, rx, ry):
    if x > rx and y > ry:
        return 1
    elif x < rx and y > ry:
        return 2
    elif x < rx and y < ry:
        return 3
    else:
        return 4


n = int(input())

qx, qy = list(map(int, input().split()))
kx, ky = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))

if quadrant(kx, ky, qx, qy) == quadrant(cx, cy, qx, qy):
    print("YES")
else:
    print("NO")

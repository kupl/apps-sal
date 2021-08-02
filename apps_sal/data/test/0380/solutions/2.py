ax, ay = list(map(int, input().split()))
bx, by = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))
if (ax == bx == cx) or (ay == by == cy):
    ans = 1
elif (ax == bx) and ((cy <= min(ay, by)) or (cy >= max(ay, by))):
    ans = 2
elif (ax == cx) and ((by <= min(ay, cy)) or (by >= max(ay, cy))):
    ans = 2
elif (cx == bx) and ((ay <= min(cy, by)) or (ay >= max(cy, by))):
    ans = 2
elif (ay == by) and ((cx <= min(ax, bx)) or (cx >= max(ax, bx))):
    ans = 2
elif (ay == cy) and ((bx <= min(ax, cx)) or (bx >= max(ax, cx))):
    ans = 2
elif (cy == by) and ((ax <= min(cx, bx)) or (ax >= max(cx, bx))):
    ans = 2
else:
    ans = 3
print(ans)

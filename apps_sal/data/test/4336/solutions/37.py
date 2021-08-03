W, H, x, y = map(int, input().split())
ans1 = W * H / 2
cen_x, cen_y = W / 2, H / 2
if cen_x == x and cen_y == y:
    ans2 = 1
else:
    ans2 = 0
print(str(ans1) + " " + str(ans2))

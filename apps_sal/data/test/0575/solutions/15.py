n = int(input())
(ax, ay) = [int(x) for x in input().split()]
(bx, by) = [int(x) for x in input().split()]
(cx, cy) = [int(x) for x in input().split()]


if (bx < ax < cx) or (bx > ax > cx) or (by < ay < cy) or (by > ay > cy):
    print("NO")
else:
    print("YES")

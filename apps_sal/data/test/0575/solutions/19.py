n = int(input())
(ax, ay) = list(map(int, input().split()))
(bx, by) = list(map(int, input().split()))
(cx, cy) = list(map(int, input().split()))
if (ax - bx) * (ax - cx) > 0 and (ay - by) * (ay - cy) > 0:
    print('YES')
else:
    print('NO')

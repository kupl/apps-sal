n = int(input())

ax, ay = map(int, input().split())
bx, by = map(int, input().split())

cx, cy = map(int, input().split())

if ((bx < ax and cx < ax) or (bx > ax and cx > ax)) and ((by < ay and cy < ay) or (by > ay and cy > ay)):
    print('YES')

else:
    print('NO')

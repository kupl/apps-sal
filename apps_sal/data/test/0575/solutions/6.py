# make sure the king never crosses the row or column the queen is in

n = int(input())
ax, ay = list(map(int, input().split()))
bx, by = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))

if bx < ax < cx or bx > ax > cx or by < ay < cy or cy < ay < by:
    print('NO')
else:
    print('YES')


t, sx, sy, ex, ey = map(int, input().split())
dx, dy = 'E' if ex - sx >= 0 else 'W', 'N' if ey - sy > 0 else 'S'
mx, my = abs(ex - sx), abs(ey - sy)
for i, ch in enumerate(input()):
    if ch == dx and mx > 0:
        mx -= 1
    elif ch == dy and my > 0:
        my -= 1
    if mx == 0 and my == 0:
        print(i + 1)
        return
print(-1)

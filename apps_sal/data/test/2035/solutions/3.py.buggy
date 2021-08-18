import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

n, sx, sy = list(map(int, input().split()))
s = [0, 0, 0, 0]
for i in range(n):
    x, y = list(map(int, input().split()))
    if x < sx:
        s[0] += 1
    elif sx < x:
        s[1] += 1
    if y < sy:
        s[2] += 1
    elif sy < y:
        s[3] += 1
s = [(s[i], i)for i in range(4)]
s.sort(key=lambda x: -x[0])
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(4):
    ans, j = s[i]
    px, py = sx + dxdy[j][0], sy + dxdy[j][1]
    if 0 <= px <= 10**9 and 0 <= py <= 10**9:
        print(ans)
        print(px, py)
        return

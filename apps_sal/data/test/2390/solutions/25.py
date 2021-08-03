import sys
input = sys.stdin.readline
N, C = map(int, input().split())
XV = [tuple(map(int, input().split())) for i in range(N)]

rcum1 = [0]
rcum2 = [0]
rcummx = [0]
px = 0
for x, v in XV:
    d = x - px
    rcum1.append(rcum1[-1] + v - d)
    rcum2.append(rcum2[-1] + v - 2 * d)
    rcummx.append(max(rcummx[-1], rcum1[-1]))
    px = x

lcum1 = [0]
lcum2 = [0]
lcummx = [0]
px = C
for x, v in reversed(XV):
    d = px - x
    lcum1.append(lcum1[-1] + v - d)
    lcum2.append(lcum2[-1] + v - 2 * d)
    lcummx.append(max(lcummx[-1], lcum1[-1]))
    px = x
lcum1.reverse()
lcum2.reverse()
lcummx.reverse()

ans = max(rcummx[-1], lcummx[0])
for i in range(N + 1):
    a = rcum2[i] + lcummx[i]
    b = lcum2[i] + rcummx[i]
    ans = max(ans, a, b)
print(ans)

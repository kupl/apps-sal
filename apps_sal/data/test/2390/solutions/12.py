n, c = list(map(int, input().split()))
xv = [list(map(int, input().split())) for _ in range(n)]

cw = []
cw2 = [0]
v_sm = 0
for x, v in xv:
    v_sm += v
    cw.append(v_sm - x)
    cw2.append(v_sm - 2 * x)

ccw = []
ccw2 = [0]
v_sm = 0
for x, v in xv[::-1]:
    v_sm += v
    ccw.append(v_sm - (c - x))
    ccw2.append(v_sm - 2 * (c - x))

cw_mx = [0]
ccw_mx = [0]
for e in cw:
    cw_mx.append(max(cw_mx[-1], e))
for e in ccw:
    ccw_mx.append(max(ccw_mx[-1], e))

ans = 0
for i, e in enumerate(cw2):
    mx = e + ccw_mx[n - i]
    ans = max(ans, mx)

for i, e in enumerate(ccw2):
    mx = e + cw_mx[n - i]
    ans = max(ans, mx)

print(ans)

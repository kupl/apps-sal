from math import ceil
N, D, A = map(int, input().split())
XH = [list(map(int, input().split())) for i in range(N)]
XH.sort()
times = ceil(XH[0][1] / A)
ans = times
damege = [times * A]
coor = [XH[0][0] + 2 * D]
start = 0
end = 1
dam = sum(damege[start:end])
for i in range(1, N):
    st = start
    while start < end and coor[start] < XH[i][0]:
        start += 1
    dam -= sum(damege[st:start])
    H = XH[i][1] - dam
    if H > 0:
        times = ceil(H / A)
        ans += times
        damege.append(times * A)
        dam += times * A
        coor.append(XH[i][0] + 2 * D)
        end += 1
print(ans)

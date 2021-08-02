N, H = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N)]
ab = list(zip(*ab))
a = sorted(ab[0], reverse=True)
b = sorted(ab[1], reverse=True)
amax = a[0]
bc = 0
ans = 0
flag = True
while H > 0 and flag:
    bmax = b[bc]
    if bmax > amax:
        H -= bmax
        bc += 1
        if bc == N:
            flag = False
        ans += 1
    else:
        flag = False
if H > 0:
    ans += (H + amax - 1) // amax
print(ans)

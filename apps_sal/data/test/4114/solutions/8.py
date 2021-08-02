N = int(input())
XYH_list = [list(map(int, input().split())) for i in range(N)]
XYH_list = sorted(XYH_list, key=lambda x: x[2], reverse=True)

for xi in range(0, 101):
    for yi in range(0, 101):
        tmpH = 0
        for k in range(N):
            x, y, h = XYH_list[k]
            if k == 0:
                tmpH = h + abs(x - xi) + abs(y - yi)
            if h == max((tmpH - abs(x - xi) - abs(y - yi)), 0):
                if k == N - 1:
                    ans = [str(xi), str(yi), str(tmpH)]
                continue
            else:
                break
print(' '.join(ans))

n = int(input())
XYH = [list(map(int, input().split())) for _ in range(n)]
# print(XYH)

for x1, y1, h1 in XYH:
    if h1 > 0:
        for Cx in range(101):
            for Cy in range(101):
                H = h1 + abs(x1 - Cx) + abs(y1 - Cy)
                # print(Cx, Cy, H)
                if all(h == max(H - abs(x - Cx) - abs(y - Cy), 0) for x, y, h in XYH):
                    print(Cx, Cy, H)
                    return

N = int(input())
xyp = []
xym = []
for _ in range(N):
    (x, y) = map(int, input().split())
    xyp.append(x + y)
    xym.append(x - y)
xyp.sort()
xym.sort()
print(max(xyp[-1] - xyp[0], xym[-1] - xym[0]))

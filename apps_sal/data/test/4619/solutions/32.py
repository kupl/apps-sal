(W, H, N) = map(int, input().split())
array = [list(map(int, input().split())) for i in range(N)]
xmin = 0
xmax = W
ymin = 0
ymax = H
for i in range(N):
    if array[i][2] == 1:
        xmin = max(xmin, array[i][0])
    elif array[i][2] == 2:
        xmax = min(xmax, array[i][0])
    elif array[i][2] == 3:
        ymin = max(ymin, array[i][1])
    elif array[i][2] == 4:
        ymax = min(ymax, array[i][1])
area = (xmax - xmin) * (ymax - ymin)
if area <= 0 or xmax < xmin or ymax < ymin:
    print(0)
else:
    print(area)

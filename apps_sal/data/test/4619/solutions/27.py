W, H, N = map(int, input().split())
x, y, a = [0] * N, [0] * N, [0] * N
for i in range(N):
    x[i], y[i], a[i] = map(int, input().split())
    
xmin = 0
xmax = W
ymin = 0
ymax = H

for i in range(N):
    if a[i] == 1:
        xmin = max(x[i], xmin)
    elif a[i] == 2:
        xmax = min(x[i], xmax)
    elif a[i] == 3:
        ymin = max(y[i], ymin)
    else:
        ymax = min(y[i], ymax)

height = ymax - ymin
width = xmax - xmin

if height <= 0 or width <= 0:
    print(0)
else:
    print(height * width)

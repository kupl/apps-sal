h, w, m = map(int, input().split())
bord_x, bord_y = [0]*h, [0]*w
 
hw = []
for _i in range(m):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    bord_x[s] += 1
    bord_y[t] += 1
    hw.append([s, t])
 
x_max, y_max = max(bord_x), max(bord_y)
 
cnt = 0
for i, j in hw:
    if bord_x[i] == x_max and bord_y[j] == y_max:
        cnt += 1
 
if cnt == bord_x.count(x_max)*bord_y.count(y_max):
    x_max -= 1
 
print(x_max+y_max)

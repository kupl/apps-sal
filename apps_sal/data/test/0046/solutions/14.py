x, y = map(int, input().split())
arx = []
ary = []
xx = x // 5
arx = [xx, xx, xx, xx, xx]
for i in range(x % 5):
    arx[i] += 1
yy = y // 5
ary = [yy, yy, yy, yy, yy]
for i in range(y % 5):
    ary[i] += 1
sum = 0
sum += arx[0] * ary[3]
sum += arx[1] * ary[2]
sum += arx[2] * ary[1]
sum += arx[3] * ary[0]
sum += arx[4] * ary[4]
print(sum)

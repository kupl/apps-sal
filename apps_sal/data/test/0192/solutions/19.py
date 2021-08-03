c = 0
d = 0


t = input().split()
x = int(t[0])
y = int(t[1])

xx = [y, y, y]
yy = [x, x, x]
while(yy != xx):
    xx.sort()
    z = sum(xx[1:3]) - 1
    c = c + 1
    if(z >= x):
        xx[0] = x

    else:
        xx[0] = z

print(c)

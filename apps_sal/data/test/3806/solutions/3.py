s = input().split()
n = int(s[0])

px = int(s[1])
py = int(s[2])


y = []
x = []

for i in range(n):
    s = input().split()
    x.append(int(s[0]) - px)
    y.append(int(s[1]) - py)
    # print(x[i],y[i])

l = []
x0, y0 = x[-1], y[-1]

for i in range(n):
    l.append(x[i] * x[i] + y[i] * y[i])
    dx, dy = x[i] - x0, y[i] - y0
    if (x0 * dx + y0 * dy) * (x[i] * dx + y[i] * dy) < 0:
        x0 = x0 * y[i] - x[i] * y0
        l.append(x0 * x0 / (dx * dx + dy * dy))
    x0, y0 = x[i], y[i]

a = 3.141592653589793 * (max(l) - min(l))
#print (px,py)
#print (x[imax],y[imax])
#print (x[imin],y[imin])
#print (((px - x[imax])*(px - x[imax]) + (py - y[imax])*(py - y[imax])))
#print (((px - x[imin])*(px - x[imin]) + (py - y[imin])*(py - y[imin])))

print(a)

def is_parallel(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2

def is_diagonal(x1, y1, x2, y2):
    return abs(x1 - x2) == abs(y1 - y2)

n = int(input())
xs = input().split(" ")
x0 = int(xs[0])
y0 = int(xs[1])

inf = 1000000000000000000
mins = [inf, inf, inf, inf, inf, inf, inf, inf]
#       <-    ^    ->   v    NE   SE   SW   NW
minx = ['B', 'B', 'B', 'B', 'R', 'R', 'R', 'R']

for i in range(0, n):
    xs = input().split(" ")
    t = xs[0]
    x = int(xs[1])
    y = int(xs[2])

    if (is_parallel(x0, y0, x, y)):
        if (y > y0):
            if (y - y0 < mins[1]):
                mins[1] = y - y0
                minx[1] = t
        elif (y < y0):
            if (y0 - y < mins[3]):
                mins[3] = y0 - y
                minx[3] = t
        elif (x > x0):
            if (x - x0 < mins[2]):
                mins[2] = x - x0
                minx[2] = t
        else:
            if (x0 - x < mins[0]):
                mins[0] = x0 - x
                minx[0] = t
    elif (is_diagonal(x0, y0, x, y)):
        if (x > x0 and y > y0):
            if (x - x0 < mins[4]):
                mins[4] = x - x0
                minx[4] = t
        elif (x > x0 and y < y0):
            if (x - x0 < mins[5]):
                mins[5] = x - x0
                minx[5] = t
        elif (x < x0 and y < y0):
            if (x0 - x < mins[6]):
                mins[6] = x0 - x
                minx[6] = t
        else:
            if (x0 - x < mins[7]):
                mins[7] = x0 - x
                minx[7] = t

if (minx[0] != 'B' or minx[1] != 'B' or minx[2] != 'B' or minx[3] != 'B' or minx[4] != 'R' or minx[5] != 'R' or minx[6] != 'R' or minx[7] != 'R'):
    print ("YES")
else:
    print ("NO")



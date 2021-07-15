import sys
f = sys.stdin
#f = open("input.txt", "r")
line = [int(i) for i in f.read().strip().split()]
x, y = line[0], line[1]
x1, x2 = 0, abs(x)+abs(y)
y1, y2 = abs(x)+abs(y), 0
if x<0 and y>0:
    x1, y1 = y1*-1, x1
    x2, y2 = y2*-1, x2
elif x>0 and y<0:
    y1 *= -1
elif x<0 and y<0:
    x1, x2 = x2*-1, x1
    y1, y2 = y2, y1*-1
print(x1,y1,x2,y2)

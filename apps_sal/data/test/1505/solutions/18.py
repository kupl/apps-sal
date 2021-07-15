from math import sqrt

px, py, vx, vy, a, b, c, d = (int(x) for x in input().split())

veclen = sqrt(vx**2 + vy**2)

newvx = b/veclen * vx
newvy = b/veclen * vy

point1x = px + newvx
point1y = py + newvy

newvx, newvy = -newvy, newvx

veclen = sqrt(newvx**2 + newvy**2)

newvx = (a/2)/veclen * newvx
newvy = (a/2)/veclen * newvy

point2x = px + newvx
point2y = py + newvy

point7x = px - newvx
point7y = py - newvy

veclen = sqrt(newvx**2 + newvy**2)

newvx = (c/2)/veclen * newvx
newvy = (c/2)/veclen * newvy

point3x = px + newvx
point3y = py + newvy

point6x = px - newvx
point6y = py - newvy

newvx, newvy = -newvy, newvx

veclen = sqrt(newvx**2 + newvy**2)

newvx = (d)/veclen * newvx
newvy = (d)/veclen * newvy

point4x = point3x + newvx
point4y = point3y + newvy

point5x = point6x + newvx
point5y = point6y + newvy

print(str(point1x)+" "+str(point1y))
print(str(point2x)+" "+str(point2y))
print(str(point3x)+" "+str(point3y))
print(str(point4x)+" "+str(point4y))
print(str(point5x)+" "+str(point5y))
print(str(point6x)+" "+str(point6y))
print(str(point7x)+" "+str(point7y))

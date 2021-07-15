3

import math
# from matplotlib import pyplot as plt

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def length(self):
		return math.hypot(self.x, self.y)

	def dot(self, other):
		return self.x * other.x + self.y * other.y

	def angleWith(self, other):
		return math.acos( self.dot(other) / (self.length() * other.length()) )

	def normalize(self):
		self /= self.length()

	def normalized(self):
		return self / self.length()

	def rotate(self, angle):
		sine = math.sin(angle)
		cosine = math.cos(angle)
		x = self.x * cosine - self.y * sine
		y = self.x * sine + self.y * cosine

		self.x = x
		self.y = y

	def rotated(self, angle):
		sine = math.sin(angle)
		cosine = math.cos(angle)
		x = self.x * cosine - self.y * sine
		y = self.x * sine + self.y * cosine

		return Vector(x, y)

	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		return self

	def __isub__(self, other):
		self.x -= other.x
		self.y -= other.y
		return self

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y)

	def __imul__(self, other):
		self.x *= other
		self.y *= other
		return self

	def __itruediv__(self, other):
		self.x /= other
		self.y /= other
		return self

	def  __mul__(self, other):
		return Vector(self.x * other, self.y * other)

	def __truediv__(self, other):
		return Vector(self.x / other, self.y / other)

	def __neg__(self):
		return Vector(-self.x, -self.y)

	def __str__(self):
		return str(self.x) + ' ' + str(self.y)
		# return "{:.2f} {:.2f}".format(self.x, self.y)

def point_coord(n, r, i):
	d_angle = 2*math.pi / n

	return Vector(0, r).rotated(-i*d_angle)

# def line_intersection(p0, p1, p2, p3):
# 	# xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
# 	# ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

# 	dx = (p0.x - p2.x, p1.x - p3.x)
# 	dy = (p0.y - p2.y, p1.y - p3.y)

# 	def det(a, b):
# 		return a[0] * b[1] - a[1] * b[0]

# 	div = det(dx, dy)
# 	if div == 0:
# 		raise Exception('lines do not intersect')

# 	line1 = ((p0.x, p0.y), (p1.x, p1.y))
# 	line2 = ((p2.x, p2.y), (p3.x, p3.y))

# 	d = ( det(*line1), det(*line2) )

# 	x = det(d, dx) / div
# 	y = det(d, dy) / div
# 	return Vector(x, y)

def line_intersection(line1, line2):
	xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
	ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) #Typo was here

	def det(a, b):
		return a[0] * b[1] - a[1] * b[0]

	div = det(xdiff, ydiff)
	if div == 0:
		raise Exception('lines do not intersect')

	d = (det(*line1), det(*line2))
	x = det(d, xdiff) / div
	y = det(d, ydiff) / div
	return x, y

# print(line_intersection(((0,0), (4,4)), ((1,3), (3,1))))
# print(line_intersection(Vector(0,0), Vector(4,4), Vector(1,3), Vector(3,1)))

n, r = [int(i) for i in input().split()]

# n = 7
# r = 10

from1 = 0
from2 = 1
to1 = n//2
to2 = to1 + 2

# p = []
# for i in range(n):
# 	p.append(point_coord(n, r, i))

# x = [i.x for i in p]
# y = [i.y for i in p]

# plt.scatter(x, y)
# plt.axis('equal')
# plt.show()

p0 = point_coord(n, r, from1)
p1 = point_coord(n, r, from2)
p2 = point_coord(n, r, to1)
p3 = point_coord(n, r, to2)

# plt.plot([p0.x, p2.x], [p0.y, p2.y])
# plt.plot([p1.x, p3.x], [p1.y, p3.y])

# print(p0)
# print(p1)
# print(p2)
# print(p3)

v1 = p2 - p0
v2 = p3 - p1

# phi = v1.angleWith(v2)
# # omega = math.pi - phi
# print(phi)

line1 = ((p0.x, p0.y), (p2.x, p2.y))
line2 = ((p1.x, p1.y), (p3.x, p3.y))

# p_int =line_intersection(p0, p1, p2, p3)
x,y =line_intersection(line1, line2)
p_int = Vector(x, y)
# print(p_int)
# plt.scatter([p_int.x], [p_int.y], c='r')
# plt.show()

a = p_int.length()
# print(a)
theta = math.pi / n
# print(theta)
s = 0.5*r*a*math.sin(theta)
print(2*n*s)

# print(p_int)
# print(p0)
# print(p_int - p0)
# print(d)
# print()

# s = 0.5 * d * d * phi
# print(s)
# print(math.pi*r*r - n*s)


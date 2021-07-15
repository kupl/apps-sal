import math
 
eps = 1e-9
 
def sign(n):
    if n > eps: return 1
    if n < -eps: return -1
    return 0
 
def cross(a, b):
    return a.x * b.y - a.y * b.x
 
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)
    
    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y)
    
    def length(self):
        return math.hypot(self.x, self.y)
 
def solve(polygon, p, q):
    intersections = []
    for (a, b) in zip(polygon, polygon[1:] + polygon[:1]):
        ss = sign(cross(a - p, q - p))
        es = sign(cross(b - p, q - p))
 
        if ss == es: continue
 
        t = cross(a - p, a - b) / cross(q - p, a - b)
        intersections.append((t, es - ss))
    intersections = sorted(intersections)
    total_t, previous_t, count = [0] * 3
    
    for t, order in intersections:
        if (count > 0): total_t += t - previous_t
        previous_t = t
        count += order
    # print(total_t) 
 
    print(total_t * (q - p).length())
    
n, m = map(int, input().split())
 
polygon = []
for i in range(n):
    x, y = map(float, input().split())
    polygon.append(Vector(x, y))
area = sum(map(lambda x: cross(x[0], x[1]), zip(polygon, polygon[1:] + polygon[:1])))
if (area < 0): polygon.reverse()
 
for i in range(m):
    x1, y1, x2, y2 = map(float, input().split())
    solve(polygon, Vector(x1, y1), Vector(x2, y2))

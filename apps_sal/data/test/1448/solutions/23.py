class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, begin, end):
        self.x = end.x - begin.x
        self.y = end.y - begin.y

    def mult(self, other):
        return self.x * other.y - self.y * other.x


n, d = list(map(int, input().split()))
m = int(input())
ans = []
vector1 = Vector(Point(d, 0), Point(0, d))
vector2 = Vector(Point(d, 0), Point(n, n - d))
vector3 = Vector(Point(n - d, n), Point(0, d))
vector4 = Vector(Point(n - d, n), Point(n, n - d))
for i in range(m):
    x, y = list(map(int, input().split()))
    vector15 = Vector(Point(d, 0), Point(x, y))
    vector35 = Vector(Point(n - d, n), Point(x, y))
    if (vector15.mult(vector1) * vector15.mult(vector2) <= 0) and (vector35.mult(vector3) * vector35.mult(vector4) <= 0):
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __sub__(self, other):
        # print("return sub", self)
        return Point(self.x - other.x, self.y - other.y)


def cross(a, b):
    return a.x * b.y - b.x * a.y


n = int(input())
points = []
for _ in range(n):
    x_, y_ = map(int, input().strip().split())
    p = Point(x_, y_)
    points.append(p)


def check(used):
    nonlocal n, points
    f = -1
    s = -1
    for i in range(n):
        if not used[i]:
            if f == -1:
                f = i
            elif s == -1:
                s = i
    if s == -1:
        return True
    for i in range(n):
        if not used[i]:
            if cross(points[f] - points[s], points[i] - points[f]) != 0:
                return False
    return True


def solve(a, b):
    nonlocal n, points
    used = [False] * n
    for i in range(n):
        if cross(a - b, points[i] - a) == 0:
            used[i] = True

    return check(used)


def solution():
    nonlocal points
    if len(points) <= 2:
        print('YES')
        return
    ans = False
    if (solve(points[0], points[1]) or solve(points[0], points[2]) or solve(points[1], points[2])):
        ans = True

    if ans:
        print("YES")
    else:
        print('NO')


solution()

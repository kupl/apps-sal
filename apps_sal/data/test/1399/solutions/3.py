import sys
from math import gcd


class Segment:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def dx(self):
        return self.x2 - self.x1
    
    def dy(self):
        return self.y2 - self.y1
    
    def pt_cnt(self):
        return gcd(abs(self.dx()), abs(self.dy())) + 1
    
    def A(self):
        return self.y1 - self.y2
    
    def B(self):
        return self.x2 - self.x1

    def C(self):
        return -self.A() * self.x1 - self.B() * self.y1

    def inner_x(self, x):
        l = self.x1
        r = self.x2
        if l > r:
            l, r = r, l
        return l <= x <= r
    
    def inner_y(self, y):
        l = self.y1
        r = self.y2
        if l > r:
            l, r = r, l
        return l <= y <= r
    
    def inner(self, x, y):
        return self.inner_x(x) and self.inner_y(y)

    def intersect(self, other):
        dx = det(self.C(), self.B(), other.C(), other.B())
        dy = det(self.A(), self.C(), other.A(), other.C())
        d = det(self.A(), self.B(), other.A(), other.B())
        if d == 0:
            return False, 0, 0
        if dx % d != 0 or dy % d != 0:
            return False, 0, 0
        x = -dx // d
        y = -dy // d
        if not self.inner(x, y) or not other.inner(x, y):
            return False, 0, 0
        return True, x, y


def det(a, b, c, d):
    return a * d - b * c

def main():
    n = int(input())
    segments = []
    ans = 0
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        segment = Segment(x1, y1, x2, y2)
        ans += segment.pt_cnt()
        pt = set()
        for other in segments:
            result, x, y = segment.intersect(other)
            if result:
                pt.add((x, y))
        ans -= len(pt)
        segments.append(segment)  
    print(ans)
        
def __starting_point():
    main()
__starting_point()

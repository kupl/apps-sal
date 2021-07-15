import math


class Pt:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __sub__(self, other):
        return Pt(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __xor__(self, other):
        return self.x * other.y - self.y * other.x

    def len(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


n = int(input())
data = []
for i in range(n):
    data.append(Pt(*list(map(int, input().split()))))
min_ = 10 ** 10
for i in range(1, n - 1):
    A = data[i - 1]
    B = data[i + 1]
    C = data[i]
    r = abs((C - A) ^ (B - A)) / (B - A).len()
    min_ = min(min_, r)
A = data[0]
B = data[n - 2]
C = data[n - 1]
r = abs((C - A) ^ (B - A)) / (B - A).len()
min_ = min(min_, r)
A = data[1]
B = data[n - 1]
C = data[0]
r = abs((C - A) ^ (B - A)) / (B - A).len()
min_ = min(min_, r)
print(min_ / 2)


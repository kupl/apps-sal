from decimal import Decimal

RESULT = 0


class Glass:
    def __init__(self):
        self.left = None
        self.right = None
        self.amount = Decimal(0)
        self.is_calculated = False

    def add_wine(self, amount):
        extra_amount = self.amount + amount - Decimal(1)
        if extra_amount > 0:
            self.amount = Decimal(1)
            if self.left is not None:
                self.left.add_wine(extra_amount / Decimal(2))
            if self.right is not None:
                self.right.add_wine(extra_amount / Decimal(2))
        else:
            self.amount += amount


def calculate(glass: Glass):
    if glass.is_calculated:
        return

    nonlocal RESULT
    if glass.amount == Decimal(1):
        RESULT += 1
    glass.is_calculated = True

    if glass.left is not None:
        calculate(glass.left)
    if glass.right is not None:
        calculate(glass.right)

n, t = list(map(int, input().split()))

a = []

for _ in range(n):
    a.append([])

for i in range(n, 0, -1):
    # a[i-1].extend([Glass()] * i)
    for _ in range(i):
        a[i-1].append(Glass())
    if i != n:
        for j, g in enumerate(a[i-1]):
            g.left = a[i][j]
            g.right = a[i][j+1]

a[0][0].add_wine(t)

calculate(a[0][0])

print(RESULT)


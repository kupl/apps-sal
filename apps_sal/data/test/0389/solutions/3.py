import math
import fractions
a, b = list(map(int, input().split()))
a2 = 0
a3 = 0
a5 = 0
b2 = 0
b3 = 0
b5 = 0
while a % 2 == 0:
    a = a / 2
    a2 = a2 + 1
while a % 3 == 0:
    a = a / 3
    a3 = a3 + 1
while a % 5 == 0:
    a = a / 5
    a5 = a5 + 1
while b % 2 == 0:
    b = b / 2
    b2 = b2 + 1
while b % 3 == 0:
    b = b / 3
    b3 = b3 + 1
while b % 5 == 0:
    b = b / 5
    b5 = b5 + 1
if a != b:
    print(-1)
else:
    print(math.ceil(math.fabs(b2 - a2) + math.fabs(b5 - a5) + math.fabs(b3 - a3)))

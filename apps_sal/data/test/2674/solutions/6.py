import math
P = input()
a, b, c = P[0], P[1], P[2]
if (int(a) | int(b) | int(c)) > 0 and (int(a) ^ int(b) ^ int(c)) > 0:
    print("Inclusive")
else:
    print("Exclusive")

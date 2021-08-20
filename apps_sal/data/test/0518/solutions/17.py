from math import pi, sin
(n, r) = list(map(float, input().split()))
ang = pi / n
k = sin(ang)
print(k * r / (1 - k))

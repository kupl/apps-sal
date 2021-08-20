from math import sqrt, floor
(a, b) = list(map(int, input().split()))
q = floor(sqrt(a))
w = floor((sqrt(4 * b + 1) - 1) / 2)
print('Vladik' if q <= w else 'Valera')

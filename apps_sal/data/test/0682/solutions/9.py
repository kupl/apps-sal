__author__ = 'widoc'

r1, c1, r2, c2 = list(map(int, input().split()))

a1 = 1 if r1 == r2 or c1 == c2 else 2
a2 = 0
if abs(r1-r2) == abs(c1-c2):
    a2 = 1
elif (abs(r1-r2) + abs(c1-c2)) % 2 == 0:
    a2 = 2
a3 = max(abs(r1-r2),abs(c1-c2))

print(a1, a2, a3)



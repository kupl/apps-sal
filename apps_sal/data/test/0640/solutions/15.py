import sys
inp = list(map(int, sys.stdin.readline().split()))
a = inp[0]
b = inp[1]
f = 0
d = 0
s = 0
for dice in range(1, 6 + 1):
    A = abs(dice - a)
    B = abs(dice - b)
    if A < B:
        f += 1
    if A > B:
        s += 1
    if A == B:
        d += 1
print(f, d, s)

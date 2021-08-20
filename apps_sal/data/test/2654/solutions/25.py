from numpy import *
t = loadtxt(open(0), skiprows=1)
(a, b) = median(t, 0)
print(int((b - a) * (2 - len(t) % 2)) + 1)

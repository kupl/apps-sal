import sys
(a, b, c, d) = sys.stdin.readline().strip().split(' ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)
res_max = max(a * c, a * d, b * c, b * d)
print(res_max)

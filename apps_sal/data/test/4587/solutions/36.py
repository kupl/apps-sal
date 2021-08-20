from bisect import *
((n,), a, b, c) = [sorted(map(int, o.split())) for o in open(0)]
print(sum((bisect_left(a, i) * (n - bisect(c, i)) for i in b)))

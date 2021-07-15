#!/usr/bin/env python3
import math
t, a, b = list(map(int,input().split()))
l= a * b // math.gcd(a,b)
p = (t // l) * min(a,b) + min(t % l, min(a,b) - 1)
q = t
r = math.gcd(p, q)
print('{}/{}'.format(p//r, q//r))


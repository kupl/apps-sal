from sys import stdin, stdout
from bisect import *
input = stdin.read()
(n, ai_str, m, qi_str) = [_f for _f in input.split('\n') if _f]
a = list(map(int, ai_str.split()))
q = list(map(int, qi_str.split()))
assert len(a) > 0 and len(q) > 0
b = [0] * len(a)
for (i, ai) in enumerate(a):
    b[i] = b[i - 1] + ai
for qi in q:
    print(bisect_left(b, qi) + 1)

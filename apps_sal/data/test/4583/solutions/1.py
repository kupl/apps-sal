import itertools
import sys
sys.setrecursionlimit(10**6)

a, b, c, d = [int(i) for i in str(input())]

for i, j, k in itertools.product([1, -1], repeat=3):
    if a + b * i + c * j + d * k == 7:
        break

if i == 1:
    i = "+"
else:
    i = "-"
if j == 1:
    j = "+"
else:
    j = "-"
if k == 1:
    k = "+"
else:
    k = "-"

print(("{}{}{}{}{}{}{}=7".format(a, i, b, j, c, k, d)))

from math import sqrt
n = int(input())
sq = int(sqrt(n))
s = sq * sq
if n == s:
    print(2 * sq)
elif n <= s + sq:
    print(2 * sq + 1)
else:
    print(2 * sq + 2)

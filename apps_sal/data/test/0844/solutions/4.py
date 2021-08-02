from itertools import accumulate

n = int(input())
l = accumulate([2 * int(c) - 1 for c in input()])
m = [None] * (2 * n + 1)
m[n] = -1
a = 0
for i, b in enumerate(l):
    if m[n + b] is None:
        m[n + b] = i
    else:
        a = max(a, i - m[n + b])
print(a)

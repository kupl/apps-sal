from itertools import groupby
n, a, b = [int(x) for x in input().split()]

a, b = sorted([a, b])
total = a + b

s = input().strip()

for val, g in groupby(s):
    if val == '*': continue
    length = len(list(g))
    b -= (length + 1) // 2
    a -= length // 2
    if a > b:
        a, b = b, a

a = max(a, 0)
b = max(b, 0)

print(total - a - b)

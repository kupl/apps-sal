from collections import Counter
n = int(input())
a = Counter()
for _ in range(n):
    a[int(input())] += 1

try:
    x, y = a.popitem(), a.popitem()
except KeyError:
    print('NO')
    return
if not a and x[1] == y[1]:
    print('YES')
    print(x[0], y[0])
else:
    print('NO')


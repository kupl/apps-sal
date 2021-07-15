from collections import defaultdict

n, k = list(map(int, input().split()))
a = defaultdict(int)
p = '@'
x = 0
for el in input():
    if el == p:
        x += 1
    elif p != '@':
        a[p] += (x + 1) // k
        x = 0
    p = el
if k != 0:
    a[p] += (x + 1) // k
print(max(a.values()))


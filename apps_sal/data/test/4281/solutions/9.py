from itertools import*
_, x = open(0)
x = sorted(map(int, x.split()))
i, *y = sorted(set(x))
s = {i + 1}
for i in y:
    if not(i - 1 in s or i in s):
        s.add(i + 1)
print(len(s), end=' ')
s = set()
for i, t in groupby(x):
    t = len(list(t))
    if not i - 1 in s and t:
        s.add(i - 1)
        t -= 1
    if not i in s and t:
        s.add(i)
        t -= 1
    if not i + 1 in s and t:
        s.add(i + 1)
print(len(s))

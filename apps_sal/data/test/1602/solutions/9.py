from collections import defaultdict
n = int(input())
xs = list(map(int, input().split()))
count = defaultdict(int)
for x in xs:
    for (i, b) in enumerate(reversed(bin(x)[2:])):
        if b != '0':
            count[i] += 1
rm = 0
for (k, v) in list(count.items()):
    if v > 1:
        rm += 2 ** k
m = (-1, 0)
for (i, x) in enumerate(xs):
    if (x | rm) - rm > m[0]:
        m = ((x | rm) - rm, i)
i = m[1]
xs = [xs[i]] + xs[:i] + xs[i + 1:]
print(' '.join(map(str, xs)))

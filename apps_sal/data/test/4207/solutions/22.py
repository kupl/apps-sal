from collections import Counter
from fractions import Fraction

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

c = Counter()

r = 0
for i in range(n):
    if a[i] == 0 == b[i]:
        r+=1
        continue

    if a[i]==0:
        continue

    c[Fraction(b[i], a[i])] += 1

#print(c)

r += c.most_common(1)[0][1] if len(c) > 0 else 0

print(r)

from fractions import Fraction
from math import ceil
from collections import Counter
s = input()
n = int(input())
c = Counter(s)
out = Counter()
contrib = Counter()
for letter in c:
    out[letter] = 1
    contrib[letter] = c[letter]
sum_vals = sum(out.values())
if sum_vals > n:
    print(-1)
else:
    while sum_vals < n:
        (el, _) = contrib.most_common(1)[0]
        out[el] += 1
        sum_vals += 1
        contrib[el] = ceil(Fraction(c[el], out[el]))
    print(max(contrib.values()))
    print(''.join(out.elements()))

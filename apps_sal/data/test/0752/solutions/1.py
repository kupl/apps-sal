from collections import Counter

n = int(input())
a = Counter(input() for i in range(n))
b = Counter(input() for i in range(n))
res = 0

for c in "MLS":
    res+= abs(a[c] - b[c])
    res+= abs(a["X"+c] - b["X"+c])
    res+= abs(a["XX"+c] - b["XX"+c])
    res+= abs(a["XXX"+c] - b["XXX"+c])
print(res//2)

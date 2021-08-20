from collections import Counter
(n, a) = map(int, input().split())
X = [int(x) - a for x in input().split()]
d = Counter([0])
for i in X:
    tmp = Counter()
    for (j, k) in d.items():
        tmp[i + j] += k
    d += tmp
print(d[0] - 1)

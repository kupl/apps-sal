from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
try:
    del c[0]
except KeyError:
    pass
print(len(c))

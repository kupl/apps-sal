from collections import Counter as C

_, k = map(int, input().split())
a = [int(i) for i in input().split()]

c = C(a).values()
d = len(c) - k
if 0 < d:
    print(sum(sorted(c)[:d]))
else:
    print(0)

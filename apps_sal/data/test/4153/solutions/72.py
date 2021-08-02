import collections
s = list(map(str, input()))
ans = 0
a = collections.Counter(s)
if len(a) == 1:
    print((0))
else:
    print((min(a.values()) * 2))

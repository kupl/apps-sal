import collections

w = list(input())
c = collections.Counter(w)
if all(x % 2 == 0 for x in c.values()):
    print('Yes')
else:
    print('No')

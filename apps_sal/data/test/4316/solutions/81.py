import collections
s = input()
c = collections.Counter(s)
if list(c.values()) == [2,2]:
    print('Yes')
else:
    print('No')

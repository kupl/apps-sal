import collections
s = input()
c = collections.Counter(list(s))
print('Yes' if len(c.keys()) == 2 and len(set(c.values())) == 1 else 'No')

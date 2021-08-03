import collections as c
w = input()


counts = c.Counter(w)
if all(elem % 2 == 0 for elem in counts.values()):
    print('Yes')
else:
    print('No')

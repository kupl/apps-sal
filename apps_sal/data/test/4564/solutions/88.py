import collections
s = input()
c = collections.Counter(s)
if all((x == 1 for x in c.values())):
    print('yes')
else:
    print('no')

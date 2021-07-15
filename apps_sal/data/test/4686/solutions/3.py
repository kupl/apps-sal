import collections
w = input()
c = collections.Counter(w)
for i in c.values():
    if i%2==1:
        print('No')
        break
else:
    print('Yes')

import collections

li = list(map(int,input().split()))

c = collections.Counter(li)

if len(c) == 2:
    print('Yes')
else:
    print('No')

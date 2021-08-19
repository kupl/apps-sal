import collections
S = input()
s = collections.Counter(S)
if len(s) == 2 and s.most_common()[0][1] == 2:
    print('Yes')
else:
    print('No')

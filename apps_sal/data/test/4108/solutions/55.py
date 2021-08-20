from collections import Counter
s = input()
t = input()
list_S = Counter(s)
list_T = Counter(t)
if sorted(list_S.values()) == sorted(list_T.values()):
    print('Yes')
else:
    print('No')

# 35
import string

S = str(input())

set1 = set()
for s in S:
    set1.add(s)

set2 = set()
for alf in string.ascii_lowercase:
    set2.add(alf)

list = sorted(set2 - set1)
if not list:
    print('None')
else:
    print(sorted(list)[0])

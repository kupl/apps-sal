# ABC063
from collections import Counter

S = input()
count = Counter(S)

for cnt in count.values():
    if cnt != 1:
        print('no')
        return
else:
    print('yes')

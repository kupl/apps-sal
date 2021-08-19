from collections import Counter
w = input()
d = Counter(w)
if sum(d.values()) % 2 == 0 and len([c for c in d.values() if c % 2 == 0]) == len(d):
    print('Yes')
else:
    print('No')

from collections import Counter
w = Counter([c for c in input()])
if all([v % 2 == 0 for (k, v) in w.items()]):
    print('Yes')
else:
    print('No')

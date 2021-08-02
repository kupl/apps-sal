from collections import defaultdict
S = input()
dct = defaultdict(int)
for s in S:
    dct[s] += 1
for key, val in dct.items():
    if not val == 2:
        print('No')
        return
print('Yes')

from collections import Counter
w = input()
wc = Counter(w)
for c in wc.values():
    if c % 2 == 1:
        print('No')
        break
else:
    print('Yes')

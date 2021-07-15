from collections import Counter

s = list(input())
t = list(input())

sc = Counter(s).values()
tc = Counter(t).values()

sl = Counter(sc)
tl = Counter(tc)

if sl == tl:
    print('Yes')
else:
    print('No')

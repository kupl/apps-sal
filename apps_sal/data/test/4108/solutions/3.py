from collections import Counter
S = str(input())
T = str(input())

s = Counter(S)
t = Counter(T)

if sorted(s.values()) == sorted(t.values()):
    print('Yes')
else:
    print('No')

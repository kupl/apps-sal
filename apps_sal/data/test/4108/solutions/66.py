from collections import Counter
s = Counter(list(input()))
t = Counter(list(input()))
(s1, t1) = (sorted(list(s.values())), sorted(list(t.values())))
print('Yes' if s1 == t1 else 'No')

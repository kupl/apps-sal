from collections import Counter
s = list(input())
t = list(input())
s_count = Counter(s)
t_count = Counter(t)
if sorted(s_count.values()) == sorted(t_count.values()):
    print('Yes')
else:
    print('No')

from collections import Counter
s = input()
t = input()
ss = sorted(Counter(s).values())
st = sorted(Counter(t).values())
print('Yes') if ss == st else print('No')

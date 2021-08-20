from collections import Counter
s = input()
t = input()
s_dict = Counter(s)
t_dict = Counter(t)
s_val = list(s_dict.values())
t_val = list(t_dict.values())
s_val.sort()
t_val.sort()
if s_val == t_val:
    print('Yes')
else:
    print('No')

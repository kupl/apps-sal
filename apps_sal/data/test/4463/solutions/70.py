s = input()
s_asc = ''.join(sorted(s))
t = input()
t_desc = ''.join(sorted(t, reverse=True))
if s_asc < t_desc:
    print('Yes')
else:
    print('No')

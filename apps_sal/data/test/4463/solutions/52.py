s, t = [input() for i in range(2)]
ns = ''.join(sorted(s))
nt = ''.join(sorted(t, reverse=True))
print('Yes') if ns < nt else print('No')

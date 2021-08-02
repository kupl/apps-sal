s = input()

odd_s = list(s[0::2])
even_s = list(s[1::2])

to = ['R', 'U', 'D']
te = ['L', 'U', 'D']

if set(odd_s).issubset(to) and set(even_s).issubset(te):
    print('Yes')
else:
    print('No')

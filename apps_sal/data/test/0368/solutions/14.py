r = dict()
sb = 0
sw = 0
r['Q'] = r['q'] = 9
r['B'] = r['b'] = 3
r['K'] = r['k'] = 0
r['N'] = r['n'] = 3
r['p'] = r['P'] = 1
r['R'] = r['r'] = 5

s1 = 'prqkbn'
s2 = s1.upper()

for i in range(8):
    t = input()
    for k in t:
        if k in s1:
            sb += r[k]
        else:
            if k in s2:
                sw += r[k]
if sw == sb:
    print('Draw')
elif sw > sb:
    print('White')
else:
    print('Black')

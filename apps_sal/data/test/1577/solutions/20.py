input()

d = {'A':0, 'D':0}

for c in input():
    d[c] += 1

if d['A'] > d['D']:
    print('Anton')
elif d['A'] < d['D']:
    print('Danik')
else:
    print('Friendship')


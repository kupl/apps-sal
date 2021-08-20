s = [''] * 8
for i in range(0, 8):
    s[i] = input()
white = {}
black = {}
white['Q'] = 9
white['R'] = 5
white['B'] = 3
white['N'] = 3
white['P'] = 1
white['q'] = 0
white['r'] = 0
white['b'] = 0
white['n'] = 0
white['p'] = 0
white['.'] = 0
white['K'] = 0
white['k'] = 0
black['Q'] = 0
black['R'] = 0
black['B'] = 0
black['N'] = 0
black['P'] = 0
black['q'] = 9
black['r'] = 5
black['b'] = 3
black['n'] = 3
black['p'] = 1
black['.'] = 0
black['K'] = 0
black['k'] = 0
w = 0
b = 0
for i in range(0, 8):
    for j in range(0, 8):
        w = w + white[s[i][j]]
        b = b + black[s[i][j]]
if w > b:
    print('White')
elif w < b:
    print('Black')
else:
    print('Draw')

i = 0
l = ''
while i < 8:
    l += input()
    i += 1
w = l.count('Q') * 9 + l.count('R') * 5 + l.count('B') * 3 + l.count('N') * 3 + l.count('P')
b = l.count('q') * 9 + l.count('r') * 5 + l.count('b') * 3 + l.count('n') * 3 + l.count('p')
if w > b:
    print('White')
elif b > w:
    print('Black')
else:
    print('Draw')

s = input()

if not '.' in s:
    s = s + '.'

i = 0
zer = 0
step = 0
while s[i] == '0':
    zer += 1
    i += 1
s = s[zer:]
zer = 0


i = len(s) - 1
while s[i] == '0':
    zer += 1
    i -= 1
if zer > 0:
    s = s[:-zer]
'''if not '.' in s:
	step = zer
	s = s + '.'''


i = s.index('.')

if len(s[i:]) > 1 and i == 0:
    i += 1
    step -= 1
    while s[i] == '0':
        i += 1
        step -= 1
elif i == len(s) - 1:
    i -= 1
    while s[i] == '0':
        i -= 1
        step += 1

i = s.index('.')

if len(s) == 2 and step == 0:
    print(s[0])
elif len(s[:-step - 1]) == 1 and step > 0:
    print(s[0] + 'E' + str(step))
elif len(s[:i]) == 1 and step == 0:
    print(s[0] + '.' + s[i + 1:])
elif step == 0:
    print(s[0] + '.' + s[1:i] + s[i + 1:] + 'E' + str(len(s[1:i])))
elif step > 0:
    print(s[0] + '.' + s[1:i - step] + s[i + 1:] + 'E' + str(len(s[1:i - step]) + step))
elif step < 0 and len(s[-step:]) == 1:
    print(s[-step] + s[-step + 1:] + 'E' + str(step))
elif step < 0:
    print(s[-step] + '.' + s[-step + 1:] + 'E' + str(step))

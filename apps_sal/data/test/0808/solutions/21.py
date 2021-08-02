s = input()

if not '.' in s:
    s = s + '.'

i = 0; zer = 0; step = 0
while s[i] == '0':
    zer += 1
    i += 1
s = s[zer:]
zer = 0

# print(s)

i = len(s) - 1
while s[i] == '0':
    zer += 1
    i -= 1
if zer > 0: s = s[:-zer]
'''if not '.' in s:
	step = zer
	s = s + '.'''


#print(s, step)

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
#print(s, step, i)

if len(s) == 2 and step == 0:
    print(s[0])
    #print('case 1')
elif len(s[:-step - 1]) == 1 and step > 0:
    print(s[0] + 'E' + str(step))
    #print('case 2')
elif len(s[:i]) == 1 and step == 0:
    print(s[0] + '.' + s[i + 1:])
    #print('case 3')
elif step == 0:
    print(s[0] + '.' + s[1:i] + s[i + 1:] + 'E' + str(len(s[1:i])))
    #print('case 4')
elif step > 0:
    print(s[0] + '.' + s[1:i - step] + s[i + 1:] + 'E' + str(len(s[1:i - step]) + step))
    #print('case 5')
elif step < 0 and len(s[-step:]) == 1:
    print(s[-step] + s[-step + 1:] + 'E' + str(step))
    #print('case 6')
elif step < 0:
    print(s[-step] + '.' + s[-step + 1:] + 'E' + str(step))
    #print('case 7')

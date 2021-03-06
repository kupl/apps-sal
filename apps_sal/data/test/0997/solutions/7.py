import sys
input = sys.stdin.readline
number = []
word = []
temp = []
period = 0
bad = 0
for i in input().strip() + ',':
    if i in ',;':
        if period or bad:
            word.append(''.join(temp))
        elif len(temp) == 0:
            word.append('')
        elif temp[0] == '0':
            if len(temp) == 1 or temp[1] == '.':
                number.append(''.join(temp))
            else:
                word.append(''.join(temp))
        else:
            number.append(''.join(temp))
        temp = []
        period = 0
        bad = 0
    else:
        if i == '.':
            period += 1
        elif i not in '.0123456789':
            bad += 1
        temp.append(i)
if len(number):
    print('"%s"' % ','.join(number))
else:
    print('-')
if len(word):
    print('"%s"' % ','.join(word))
else:
    print('-')

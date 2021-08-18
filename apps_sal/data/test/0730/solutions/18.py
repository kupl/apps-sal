__author__ = 'hamed1soleimani'

lines = list()
lines.append('+------------------------+')
lines.append('|
lines.append('|
lines.append('|
lines.append('|
lines.append('+------------------------+')

n=int(input())

while True:
    if n == 0:
        break
    idx=list()
    for m in range(1, 5):
        idx.append(lines[m].find('
    while True:
        if idx.count(-1) > 0:
            idx.remove(-1)
        else:
            break
    x=min(idx)
    if lines[1].find('
        lines[1]=lines[1].replace('
        n -= 1
    elif lines[2].find('
        lines[2]=lines[2].replace('
        n -= 1
    elif lines[3].find('
        lines[3]=lines[3].replace('
        n -= 1
    elif lines[4].find('
        lines[4]=lines[4].replace('
        n -= 1

for ss in lines:
    print(ss)

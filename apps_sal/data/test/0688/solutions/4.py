favornumb = {'0': 0, '1': 0, '2': 0,
             '3': 0, '4': 0, '6': 0,
             '7': 0, '8': 0}
mass = {'0': 0, '1': 0, '2': 0,
        '3': 0, '4': 0, '6': 0,
        '7': 0, '8': 0}
for i in input():
    if i == '2' or i == '5':
        favornumb['2'] += 1
    elif i == '6' or i == '9':
        favornumb['6'] += 1
    else:
        favornumb[i] += 1
for i in input():
    if i == '2' or i == '5':
        mass['2'] += 1
    elif i == '6' or i == '9':
        mass['6'] += 1
    else:
        mass[i] += 1
ans = 200
for i in ['0', '1', '2', '3', '4', '6', '7', '8']:
    if favornumb[i] == 0:
        continue
    else:
        pretend = int(mass[i] / favornumb[i])
        if pretend <= ans:
            ans = pretend
print(ans)

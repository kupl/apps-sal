N = int(input())
item = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
for n in range(N):
    S = input()
    if S == 'AC':
        item['AC'] += 1
    elif S == 'WA':
        item['WA'] += 1
    elif S == 'TLE':
        item['TLE'] += 1
    else:
        item['RE'] += 1
print('AC x', end=' ')
print(item['AC'])
print('WA x', end=' ')
print(item['WA'])
print('TLE x', end=' ')
print(item['TLE'])
print('RE x', end=' ')
print(item['RE'])

n = int(input())
li = [input() for i in range(n)]
ac = 0
wa = 0
tle = 0
re = 0
for i in li:
    if i == 'AC':
        ac += 1
    elif i == 'WA':
        wa += 1
    elif i == 'TLE':
        tle += 1
    elif i == 'RE':
        re += 1
print('AC x', ac)
print('WA x', wa)
print('TLE x', tle)
print('RE x', re)

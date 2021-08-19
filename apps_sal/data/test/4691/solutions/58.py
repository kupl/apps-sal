n = int(input())
ac = 0
wa = 0
tle = 0
re = 0
for i in range(n):
    s = input()
    if s == 'AC':
        ac += 1
    elif s == 'WA':
        wa += 1
    elif s == 'TLE':
        tle += 1
    elif s == 'RE':
        re += 1
print('AC x {}'.format(str(ac)))
print('WA x {}'.format(str(wa)))
print('TLE x {}'.format(str(tle)))
print('RE x {}'.format(str(re)))

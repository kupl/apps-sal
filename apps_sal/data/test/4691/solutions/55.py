n = int(input())
ac, wa, tle, re = 0, 0, 0, 0;

for i in range(n):
    s = input()
    if s == 'AC':
        ac += 1
    elif s == 'WA':
        wa += 1
    elif s == 'TLE':
        tle += 1
    else:
        re += 1

print('AC', 'x', ac)
print('WA', 'x', wa)
print('TLE', 'x', tle)
print('RE', 'x', re)

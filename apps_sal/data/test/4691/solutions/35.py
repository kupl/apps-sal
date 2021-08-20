n = int(input())
s = [input() for i in range(n)]
(ac, wa, tle, re) = (0, 0, 0, 0)
for s_e in s:
    if s_e == 'AC':
        ac += 1
    elif s_e == 'WA':
        wa += 1
    elif s_e == 'TLE':
        tle += 1
    elif s_e == 'RE':
        re += 1
print(f'AC x {ac}')
print(f'WA x {wa}')
print(f'TLE x {tle}')
print(f'RE x {re}')

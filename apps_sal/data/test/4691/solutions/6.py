n = int(input())
ac = wa = tle = re = 0
for i in range(n):
    st = input()
    if st == 'AC':
        ac += 1
    elif st == 'WA':
        wa += 1
    elif st == 'TLE':
        tle += 1
    else:
        re += 1
print(f'AC x {ac}\nWA x {wa}\nTLE x {tle}\nRE x {re}')

N = int(input())
ans_ac = 0
ans_wa = 0
ans_tle = 0
ans_re = 0
for i in range(N):
    S = input()
    if S == 'AC':
        ans_ac += 1
    elif S == 'WA':
        ans_wa += 1
    elif S == 'TLE':
        ans_tle += 1
    else:
        ans_re += 1
print('AC', 'x', ans_ac)
print('WA', 'x', ans_wa)
print('TLE', 'x', ans_tle)
print('RE', 'x', ans_re)

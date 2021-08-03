S = input()
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
cnt = days.index('SUN') - days.index(S)
if cnt == 0:
    print(7)
else:
    print(cnt)

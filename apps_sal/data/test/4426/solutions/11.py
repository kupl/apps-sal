week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
s = input()
ans = 7 - week.index(s)
ans = ans if ans != 0 else 7
print(ans)

T = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
S = input()
print(6 - T.index(S) if S != 'SUN' else 7)

D = ['SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON', 'SUN']
S = input()
for i, d in enumerate(D):
    if d == S:
        print(i + 1)
        return()

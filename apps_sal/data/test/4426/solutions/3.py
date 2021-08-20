S = input()
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
for i in range(7):
    if week[i] == S:
        print(7 - i)

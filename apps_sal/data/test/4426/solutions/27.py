S = input()
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
for i in range(7):
    if day[i] == S:
        print(7 - i)

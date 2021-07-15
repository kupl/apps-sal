S = input()
day_of_the_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
for i in range(len(day_of_the_week)):
    if S == day_of_the_week[i]:
        answer = 7 - i
print(answer)

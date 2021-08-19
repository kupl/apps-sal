(days_of_fine, day_befoe_exparitation, eating_day) = map(int, input().split())
if eating_day <= days_of_fine:
    print('delicious')
elif day_befoe_exparitation < eating_day <= days_of_fine + day_befoe_exparitation:
    print('safe')
else:
    print('dangerous')

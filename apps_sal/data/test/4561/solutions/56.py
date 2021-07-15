days_of_fine, day_before_expiration, eating_day = map(int, input().split())

if eating_day <= day_before_expiration:
    print('delicious')
elif day_before_expiration < eating_day <= days_of_fine + day_before_expiration:
    print('safe')
else:
    print('dangerous')

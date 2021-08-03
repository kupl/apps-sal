__author__ = 'Think'
day1 = input()
day2 = input()
days = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}
num1 = days[day1]
num2 = days[day2]
diff = (num2 - num1) % 7
if diff in [0, 2, 3]:
    print("YES")
else:
    print("NO")

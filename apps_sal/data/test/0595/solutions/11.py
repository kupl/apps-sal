def number_of_days(year):
    if year % 400 == 0:
        return 366
    if year % 4 == 0 and year % 100 != 0:
        return 366
    return 365

y = int(input())

number_of_days_in_y = number_of_days(y)

total = number_of_days(y)

while True:
    if total % 7 == 0 and number_of_days_in_y == number_of_days(y+1):
        print(y+1)
        break
    y += 1
    total += number_of_days(y)


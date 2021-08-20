def days(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 366
    return 365


y = int(input())
y_next = y + 1
first_day_next = days(y + 1) % 7
while first_day_next != 0 or days(y) != days(y_next):
    y_next += 1
    first_day_next = (first_day_next + days(y_next) % 7) % 7
print(y_next)

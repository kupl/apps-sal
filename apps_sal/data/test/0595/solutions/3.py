def days(year):
    if year % 400 == 0:
        return 366
    if year % 4 == 0 and year % 100 != 0:
        return 366
    return 365


year = int(input())
f = days(year)
t = days(year) % 7
year += 1
while True:
    if t == 0 and days(year) == f:
        print(year)
        return
    t += days(year)
    t %= 7
    year += 1

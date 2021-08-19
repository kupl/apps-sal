def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def year_days(year):
    return 365 + int(is_leap(year))


y = int(input().strip())
offset = 0
res = y
while 1:
    if offset and offset % 7 == 0 and (is_leap(y) == is_leap(res)):
        break
    offset += year_days(res) % 7
    res += 1
print(res)

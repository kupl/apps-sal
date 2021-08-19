3


def is_leap(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


def main():
    year = int(input())
    newyear = year
    delta = 0
    while newyear == year or not (delta == 0 and is_leap(year) == is_leap(newyear)):
        delta += 365 + int(is_leap(newyear))
        delta %= 7
        newyear += 1
    print(newyear)


main()

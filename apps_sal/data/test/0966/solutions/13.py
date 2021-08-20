def is_distinct(year):
    years = str(year)
    s = set()
    for c in years:
        if c in s:
            return False
        else:
            s.add(c)
    return True


def upper_distinct(year):
    year += 1
    while True:
        if is_distinct(year):
            return year
        else:
            year += 1


def main():
    first_line = input()
    first_line = first_line.split()
    year = int(first_line[0])
    print(upper_distinct(year))


main()

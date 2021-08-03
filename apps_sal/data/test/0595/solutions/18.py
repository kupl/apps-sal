y = int(input())

d = 1


def is_v(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


v = is_v(y)

while True:
    y += 1
    if is_v(y):
        d += 2
    else:
        d += 1

    if d > 7:
        d -= 7

    if d == 1 and is_v(y) == v:
        print(y)
        break

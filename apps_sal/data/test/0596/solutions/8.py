3

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isn(yyyy):
    if yyyy == 1900:
        return False
    return yyyy % 4 == 0

def toint(date):
    yyyy, mm, dd = date
    res = 0
    for y in range(1900, yyyy):
        res += 365 + isn(y)
    for m in range(1, mm):
        res += month[m] + (m == 2 and isn(yyyy))
    return res + dd

first = tuple(map(int, input().strip().split(':')))
last = tuple(map(int, input().strip().split(':')))
if last < first:
    last, first = first, last
print(toint(last) - toint(first))


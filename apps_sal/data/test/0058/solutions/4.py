n = int(input())
a = int(input())
b = int(input())
nba = 4
nbb = 2
com = 0
s = 4 * a + 2 * b
while nba > 0 or nbb > 0:
    com += 1
    x = n
    if 2 * a + b == n:
        com = 2
        break
    elif a > b:
        while x >= a and nba > 0:
            x -= a
            nba -= 1
        while x >= b and nbb > 0:
            x -= b
            nbb -= 1
    else:
        while x >= b and nbb > 0:
            x -= b
            nbb -= 1
        while x >= a and nba > 0:
            x -= a
            nba -= 1
print(com)

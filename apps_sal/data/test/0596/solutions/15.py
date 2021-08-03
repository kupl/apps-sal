def f(y, m, d):
    return 365 * y + 31 * m + d + ((y - 1) // 4 - (y - 1) // 100 + (y - 1) // 400) - ((2 + int(y % 4 != 0 or (y % 100 == 0 and y % 400 != 0))) * (m > 2) + (m > 4) + (m > 6) + (m > 9) + (m > 11))


print(abs(f(*map(int, input().split(':'))) - f(*map(int, input().split(':')))))

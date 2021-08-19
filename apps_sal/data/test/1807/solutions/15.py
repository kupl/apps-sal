(a, b) = list(map(int, input().split()))
(c, t) = (str(list(range(a, b + 1))), 0)
print(6 * c.count('0') + 2 * c.count('1') + 5 * c.count('2') + 5 * c.count('3') + 4 * c.count('4') + 5 * c.count('5') + 6 * c.count('6') + 3 * c.count('7') + 7 * c.count('8') + 6 * c.count('9'))

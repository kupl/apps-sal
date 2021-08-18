from sys import stdin

lines = list([_f for _f in stdin.read().split('\n') if _f])


def parseline(line):
    return list(map(int, line.split()))


lines = list(map(parseline, lines))

m, s = lines[0]

if 9 * m < s or (m > 1 and s == 0):
    print("-1 -1")
    return

if m == 1 and s == 0:
    minimum = [0]
else:
    minimum = []
    s1 = s
    while s1 > 0:
        digit = min(9, s1)
        minimum.append(digit)
        s1 -= digit
    if len(minimum) < m:
        minimum[-1] -= 1
        minimum += [0] * (m - len(minimum) - 1)
        minimum.append(1)

minimum = "".join(map(str, reversed(minimum)))

maximum = []
s2 = s
while s2 > 0:
    digit = min(9, s2)
    maximum.append(digit)
    s2 -= digit
maximum += [0] * (m - len(maximum))

maximum = "".join(map(str, maximum))

print(minimum, maximum)

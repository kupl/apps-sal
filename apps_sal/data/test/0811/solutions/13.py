from sys import stdin, stdout


def solve(a, b):
    result = 0
    old = 0
    while a != 0:
        result += a
        neww = (a + old) // b
        old = (a + old) % b
        a = neww
    return result


def __starting_point():
    s = stdin.readline()
    (a, b) = s.split(' ')
    a = int(a)
    b = int(b)
    result = solve(a, b)
    print(result)


__starting_point()

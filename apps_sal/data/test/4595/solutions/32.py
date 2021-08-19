import sys
input = sys.stdin.readline


def read():
    s = input().strip()
    return (s,)


def solve(s):
    (a, z) = (0, len(s) - 1)
    while s[a] != 'A':
        a += 1
    while s[z] != 'Z':
        z -= 1
    return z - a + 1


def __starting_point():
    inputs = read()
    print(solve(*inputs))


__starting_point()

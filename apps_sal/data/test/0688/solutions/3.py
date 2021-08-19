import sys
t = int(sys.stdin.readline().strip())
cubes = [int(c) for c in list(sys.stdin.readline().strip())]


def flip(d):
    if d == 6:
        return 9
    elif d == 9:
        return 6
    elif d == 2:
        return 5
    elif d == 5:
        return 2


def build(t, cubes):
    for d in str(t):
        d = int(d)
        df = flip(d)
        if d in cubes:
            cubes.remove(d)
        elif df in cubes:
            cubes.remove(df)
        else:
            return (False, cubes)
    return (True, cubes)


i = 0
while True:
    (ok, cubes) = build(t, cubes)
    if ok:
        i += 1
    else:
        break
print(i)

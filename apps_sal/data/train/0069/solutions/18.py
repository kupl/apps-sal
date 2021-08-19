def read_generator():
    while True:
        tokens = input().split(' ')
        for t in tokens:
            yield t


reader = read_generator()


def readword():
    return next(reader)


def readint():
    return int(next(reader))


def readfloat():
    return float(next(reader))


def readline():
    return input()


def solve(a, b, m):
    o = []
    new = True
    i = 0
    for c in m:
        if c == '1':
            if new:
                o.append([i, i])
                new = False
            else:
                o[len(o) - 1][1] = i
        else:
            new = True
        i += 1
    res = len(o) * a
    for i in range(1, len(o)):
        cur = o[i]
        prev = o[i - 1]
        if (cur[0] - prev[1] - 1) * b < a:
            res -= a
            res += (cur[0] - prev[1] - 1) * b
    return res


tests = readint()
for t in range(tests):
    (a, b) = (readint(), readint())
    m = readline()
    print(solve(a, b, m))

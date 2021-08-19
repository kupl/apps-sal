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


def solve(n, m, t, a):
    ss = []
    for i in range(n):
        h = sum(a[i])
        s = [-1] * (h + 73)
        s[0] = 0
        for j in range(m):
            for k in range(h + 1, -1, -1):
                if 0 < s[k] + 1 <= m // 2:
                    v = a[i][j]
                    s[k + v] = min(s[k + v], s[k] + 1)
                    if s[k + v] == -1:
                        s[k + v] = s[k] + 1
        toAdd = []
        for j in range(len(s)):
            if s[j] > -1:
                toAdd.append(j)
        ss.append(toAdd)
    res = [0] * t
    for s in ss:
        nextRes = [0] * t
        for j in range(t):
            for v in s:
                nextRes[(v + res[j]) % t] = max(res[j] + v, nextRes[(v + res[j]) % t])
        res = nextRes
    return res[0]


tests = 1
for t in range(tests):
    n = readint()
    m = readint()
    k = readint()
    a = []
    for i in range(n):
        r = []
        for j in range(m):
            r.append(readint())
        a.append(r)
    print(solve(n, m, k, a))

def vec(x):
    if x == 0:
        return [[1]]
    s = vec(x - 1)
    y = vec(x - 1)
    for i in range(2 ** (x - 1)):
        for j in range(2 ** (x - 1)):
            y[i][j] = -y[i][j]
    out = [s[i] + y[i] for i in range(2 ** (x - 1))]
    out2 = [s[i] + s[i] for i in range(2 ** (x - 1))]
    return out + out2


x = int(input())
s = vec(x)
for i in range(2 ** x):
    ret = ''
    for j in range(2 ** x):
        if s[i][j] == 1:
            ret += '+'
        else:
            ret += '*'
    print(ret)

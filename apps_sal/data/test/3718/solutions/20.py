n = int(input())
for i in range(1):
    t = [int(x) for x in input().split()]


def checkyesno():
    s = list(set(t))
    u = sorted(s)
    v = len(s)
    y = 0
    z = 0
    c = 0
    for a in range(0, v - 2):
        if (u[a] + u[a + 1] + u[a + 2]) / 3 == u[a + 1]:
            z += 1
        if u[a + 2] - u[a + 1] == u[a + 1] - u[a] == 1:
            c += 1
    if z > 0 and c > 0:
        for i in range(0, v - 1):
            if u[i] - u[i + 1] == -1:
                y += 1
    if y >= 2:
        result = 'YES'
        print(result)
    else:
        result = 'NO'
        print(result)


if len(t) < 3:
    result = 'NO'
    print(result)
elif len(list(set(t))) < 3:
    result = 'NO'
    print(result)
else:
    checkyesno()

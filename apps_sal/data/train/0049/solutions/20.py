t = int(input())
l = []
r = []
for i in range(t):
    q, w = [int(el) for el in input().split()]
    l.append(q)
    r.append(w)


def count(x):
    if x <= 1110:
        return x
    s = str(x)
    n = len(s)
    cz = 3
    out = 0
    for i in range(n - 2):
        a = int(s[i])
        k = n - i - 1

        if a > 0:
            if cz == 3:
                out = out + k * (k - 1) * (k - 2) / 6 * 9 * 9 * 9 + k * (k - 1) / 2 * 9 * 9 + k * 9
            elif cz == 2:
                out = out + k * (k - 1) / 2 * 9 * 9 + k * 9 + 1
            elif cz == 1:
                out = out + k * 9 + 1
            cz = cz - 1

            if cz == 2:
                plus = k * (k - 1) / 2 * 9 * 9 + k * 9 + 1
            elif cz == 1:
                plus = k * 9 + 1
            elif cz == 0:
                plus = 1
            out = out + plus * (a - 1)
        if cz == 0:
            break
    if cz == 0:
        out = out + 1
        return out
    if cz == 1:
        if int(s[n - 2]) > 0:
            out = out + int(s[n - 2]) + 10
        else:
            out = out + 1 + int(s[n - 1])
        return out
    out = out + int(s[n - 2:]) + 1
    return out


for i in range(t):
    a = int(count(r[i]))
    b = int(count(l[i] - 1))
    print(a - b)

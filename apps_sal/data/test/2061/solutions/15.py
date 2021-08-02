def mark(z):
    while z: z = z[0]
    return z


def mark2(z):
    while z and type(z) == list: z = z[0]
    return z


__debug = None

n, m, kk = map(int, input().split())
data = [list(input()) for i in range(n)]

ocean = []
earth = []
work = [[] for i in range(m * n)]

for k in range(m):
    if data[0][k] == '.':
        work[m * 0 + k].append(ocean)
    if data[n - 1][k] == '.':
        work[m * (n - 1) + k].append(ocean)
for i in range(1, n - 1):
    if data[i][0] == '.':
        work[m * i + 0].append(ocean)
    if data[i][m - 1] == '.':
        work[m * i + m - 1].append(ocean)

for i in range(1, n):
    for k in range(1, m):
        if data[i][k] == '.':
            z = mark(work[m * i + k])
            if i and data[i - 1][k] == '.':
                zi = mark(work[m * (i - 1) + k])
                if z is not zi:
                    if z is ocean:
                        zi.append(z)
                    else:
                        z.append(zi)
                        z = zi
            if k and data[i][k - 1] == '.':
                zk = mark(work[m * i + k - 1])
                if z is not zk:
                    if z is ocean:
                        zk.append(z)
                    else:
                        z.append(zk)

isl = {}
no = 1

for i in range(1, n - 1):
    for k in range(1, m - 1):
        if data[i][k] == '.':
            if __debug: print(i, end=" ")
            if __debug: print(k, end=": ")
            z = mark2(work[m * i + k])
            if z:
                isl[z].append((i, k))
                if __debug: print(z, end=", old")
            elif z is not ocean:
                z.append(no)
                if __debug: print(no, end=", new")
                isl[no] = [(i, k)]
                no += 1
            if __debug: print()

if __debug: print(isl)
isl_s = list(isl.values())
if __debug: print(isl_s)
isl_s.sort(key=len)
if __debug: print(isl_s)
delta = len(isl_s) - kk
if __debug: print(len(isl_s), end=" ")
if __debug: print(kk)
for t in range(delta):
    for i, k in isl_s[t]:
        data[i][k] = '*'

print(sum(map(len, isl_s[:delta])))
for i in range(n):
    print("".join(data[i]))

s = input().split()
v = int(s[0])
z = int(s[1])
n = int(s[2])
g = [int(i) for i in input().split()]
d = [int(i) for i in input().split()]
f = [int(i) for i in input().split()]
g.sort()
d.sort()
f.sort()
iterator = [0, 0, 0]
ending = [0, 0, 0]
gap = [0, 0]
count = 0
if v < 1 or z < 2 or n < 3:
    print(0)
else:
    while iterator[0] < v and iterator[1] < z and (iterator[2] < n):
        if g[iterator[0]] < d[iterator[1]] and g[iterator[0]] < f[iterator[2]]:
            max = g[iterator[0]] * 2 + 1
            v = int(s[0])
            while ending[1] < z and d[ending[1]] < max:
                ending[1] += 1
            while ending[2] < n and f[ending[2]] < max:
                ending[2] += 1
            if ending[1] - iterator[1] < 2:
                iterator[0] += 1
                continue
            elif ending[2] - iterator[2] < 3:
                iterator[0] += 1
                continue
            else:
                gap[0] = ending[1] - iterator[1]
                gap[1] = ending[2] - iterator[2]
                count += gap[0] * (gap[0] - 1) * gap[1] * (gap[1] - 1) * (gap[1] - 2) // 12
                iterator[0] += 1
        elif d[iterator[1]] < g[iterator[0]] and d[iterator[1]] < f[iterator[2]]:
            max = d[iterator[1]] * 2 + 1
            while ending[0] < v and g[ending[0]] < max:
                ending[0] += 1
            while ending[1] < z and d[ending[1]] < max:
                ending[1] += 1
            while ending[2] < n and f[ending[2]] < max:
                ending[2] += 1
            if ending[0] - iterator[0] < 1:
                iterator[1] += 1
                continue
            elif ending[1] - iterator[1] < 2:
                iterator[1] += 1
                continue
            elif ending[2] - iterator[2] < 3:
                iterator[1] += 1
                continue
            else:
                gap[0] = ending[1] - iterator[1]
                gap[1] = ending[2] - iterator[2]
                count += (ending[0] - iterator[0]) * (ending[1] - iterator[1] - 1) * gap[1] * (gap[1] - 1) * (gap[1] - 2) // 6
                iterator[1] += 1
        elif f[iterator[2]] < g[iterator[0]] and f[iterator[2]] < d[iterator[1]]:
            max = f[iterator[2]] * 2 + 1
            while ending[0] < v and g[ending[0]] < max:
                ending[0] += 1
            while ending[1] < z and d[ending[1]] < max:
                ending[1] += 1
            while ending[2] < n and f[ending[2]] < max:
                ending[2] += 1
            if ending[0] - iterator[0] < 1:
                iterator[2] += 1
                continue
            elif ending[1] - iterator[1] < 2:
                iterator[2] += 1
                continue
            elif ending[2] - iterator[2] < 3:
                iterator[2] += 1
                continue
            else:
                gap[0] = ending[1] - iterator[1]
                gap[1] = ending[2] - iterator[2]
                count += (ending[0] - iterator[0]) * gap[0] * (gap[0] - 1) * (gap[1] - 1) * (gap[1] - 2) // 4
                iterator[2] += 1
    print(count)

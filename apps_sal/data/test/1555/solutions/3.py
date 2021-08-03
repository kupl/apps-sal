def prov(mass, now):
    check = True
    for i in range(n):
        for k in range(m):
            if now[i][k] == '>' and mass[i] <= mass[n + k]:
                check = False
                break
            elif now[i][k] == '<' and mass[i] >= mass[n + k]:
                check = False
                break
            elif now[i][k] == '=' and mass[i] != mass[n + k]:
                check = False
                break
        if not check:
            break
    return check


def prog(mass, n, m):
    prov = True
    for i in range(1, m):
        for k in range(n):
            if mass[i][k] < mass[i - 1][k]:
                prov = False
                break
        if not prov:
            break
    if not prov:
        return False
    else:
        mass_new = []
        for i in range(1, m):
            mass_n = []
            for k in range(n):
                mass_n.append(mass[i][k] - mass[i - 1][k])
            mass_new.append(max(mass_n))
        arr = [1 for i in range(m)]
        now = 1
        if 1 in mass[0][:-1]:
            now += 1
            arr = [2 for i in range(m)]
        for i in range(1, m):
            now += mass_new[i - 1]
            arr[mass[i][-1]] = now
        return arr


n, m = map(int, input().split())
if n + m <= 6:
    now = []
    for i in range(n):
        now.append(input())
    ppp = True
    for i1 in range(n + m):
        for i2 in range(n + m):
            for i3 in range(n + m):
                for i4 in range(n + m):
                    for i5 in range(n + m):
                        for i6 in range(n + m):
                            mass = [i1 + 1, i2 + 1, i3 + 1, i4 + 1, i5 + 1, i6 + 1][:n + m]
                            if prov(mass, now) and ppp:
                                print('Yes')
                                print(*mass[:n])
                                print(*mass[n:])
                                ppp = False
    if ppp:
        print('No')
else:
    mass = [[] for i in range(m)]
    mass1 = [[] for i in range(n)]
    for i in range(n):
        now = input()
        for k in range(m):
            if now[k] == '<':
                mass[k].append(1)
                mass1[i].append(-1)
            elif now[k] == '=':
                mass[k].append(0)
                mass1[i].append(0)
            else:
                mass[k].append(-1)
                mass1[i].append(1)
    for i in range(m):
        mass[i].append(i)
    for i in range(n):
        mass1[i].append(i)
    mass.sort()
    mass1.sort()

    arr = prog(mass, n, m)
    arr1 = prog(mass1, m, n)
    if arr == False or arr1 == False:
        print('No')
    else:
        print('Yes')
        print(*arr1)
        print(*arr)

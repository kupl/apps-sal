n = int(input())
u = []
s = []
ok = True
for i in range(n):
    u.append(input())
    s.append(set(u[i]))
    if len(s[i]) != len(u[i]):
        print('NO')
        ok = False
        break
if ok:
    i = 0
    ok = False
    while i < len(u):
        j = i + 1
        p = False
        while j < len(u):
            z = len(s[i].intersection(s[j]))
            if u[i] in u[j]:
                u[i] = u[j]
                s[i] = s[j]
                s.pop(j)
                u.pop(j)
                p = True
                break
            elif u[j] in u[i]:
                s.pop(j)
                u.pop(j)
                j -= 1
            elif z > 0:
                if u[i][-z:] == u[j][:z]:
                    u[i] += u[j][z:]
                elif u[j][-z:] == u[i][:z]:
                    u[i] = u[j] + u[i][z:]
                else:
                    ok = True
                    break
                s[i] = set(u[i])
                u.pop(j)
                s.pop(j)
                j -= 1
                p = True
            j += 1
        if not p:
            i += 1
        if ok:
            print('NO')
            break
    if not ok:
        u.sort()
        print(''.join(u))

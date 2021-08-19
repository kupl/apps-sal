(n, m) = list(map(int, input().split(' ')))


def De(s):
    p = s.split(' ')
    return (p[0], int(p[1]) - 1, int(p[2]))


l = [[] for _ in range(m)]
t = [0] * m
for _ in range(n):
    (p, r, s) = De(input())
    if len(l[r]) < 1:
        l[r].append((p, s))
    elif len(l[r]) < 2:
        if s > l[r][0][1]:
            l[r].insert(0, (p, s))
        else:
            l[r].append((p, s))
    elif len(l[r]) < 3:
        if s > l[r][0][1]:
            l[r].insert(0, (p, s))
        elif s > l[r][1][1]:
            l[r].insert(1, (p, s))
        else:
            l[r].append((p, s))
    else:
        if s > l[r][0][1]:
            l[r].insert(0, (p, s))
        elif s > l[r][1][1]:
            l[r].insert(1, (p, s))
        elif s > l[r][2][1]:
            l[r].insert(2, (p, s))
        else:
            l[r].append((p, s))
        l[r].pop()
for i in range(m):
    if len(l[i]) > 2 and l[i][1][1] == l[i][2][1]:
        print('?')
    else:
        print(l[i][0][0], l[i][1][0])

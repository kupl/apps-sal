def ri():
    return list(map(int, input().split()))


n = int(input())

r = []
T = []
maxt = -1
for i in range(n):
    r.append(list(ri()))

r.sort(key=lambda e: (e[1], e[0]))

T.append([r[0][2], r[0][1]])
for i in range(1, n):
    tmp = r[i][2]
    l = len(T)
    for j in range(l):
        if r[i][0] >= T[-1][1]:
            T.append([tmp, r[i][1]])
            break
        else:
            tmp = max(T[-1][0] + r[i][2], tmp)
            T.pop()
    else:
        T.append([tmp, r[i][1]])


print(max(T)[0])
